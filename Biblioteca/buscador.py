# npm install string-similarity
import requests
import difflib
from traductor import Traductor
from bandera import Bandera

API_URL = "https://www.googleapis.com/books/v1/volumes"

class Buscador:

    def __init__(self) -> None:
        self.traductor= Traductor()
        self.bandera= Bandera()

    def busca_google_books(self,busqueda):
        books = []
        # recibo el resultado de la api de google libros
        response = requests.get(f"{API_URL}?q={busqueda}")
        if response.status_code == 200:
            # recibo la data como json
            data = response.json()
            if "items" in data:
                books = [
                    {
                        # "isbn": next((identifier["identifier"] for identifier in item["volumeInfo"].get("industryIdentifiers", []) if identifier["type"] == "ISBN_13"), "No ISBN"),
                        "isbns": [
                            {
                                "tipo": d['type'],
                                "isbn": d['identifier']
                            }
                            for d in item["volumeInfo"].get("industryIdentifiers", [])  # Itera sobre los identificadores ISBN
                        ],
                        "titulo": item["volumeInfo"].get("title", "No Title"),
                        "autor": ', '.join(item["volumeInfo"].get("authors", ["Unknown"])),
                        "publicacion_año": item["volumeInfo"].get("publishedDate"),
                        "descripcion": self.traductor.traducir_al_espanol(item["volumeInfo"].get("description")),
                        "categories": self.traductor.traducir_al_espanol(', '.join(item["volumeInfo"].get("categories", ["Uncategorized"]))),
                        "edad_recomendada": self.decode_maturity_rating(item["volumeInfo"].get("maturityRating")),
                        "lenguaje": item["volumeInfo"].get("language"),
                        # "informacion": item["volumeInfo"].get("previewLink", [item["volumeInfo"].get("infoLink")]),
                        "imagen": item["volumeInfo"].get("imageLinks", {}).get("thumbnail", ""),
                        "imagen_reducida": item["volumeInfo"].get("imageLinks", {}).get("smallThumbnail", ""),
                        "pais": item["saleInfo"].get("country", "Unknown"),
                        "textSnippet": item.get("searchInfo", {}).get("textSnippet", "No snippet available"),
                        # "bandera": self.bandera.obtener_url_bandera(item["volumeInfo"].get("language")),
                    }
                    for item in data["items"]
                    if self.calcular_similitud(item["volumeInfo"].get("title", ""), busqueda) >= 0.75

                ]
        return books
        
    def decode_maturity_rating(self,maturity_rating):
        if maturity_rating == 'NOT_MATURE':
            return 'Todas las Edades'
        elif maturity_rating == 'MATURE':
            return 'Solo Adultos'
        elif maturity_rating == 'PARENTAL_GUIDANCE':
            return 'Guía Parental'
        else:
            return 'Clasificación Desconocida'

    def calcular_similitud(self,titulo, palabra_buscada):
        # Compara el título con la palabra buscada y devuelve una ratio de similaridad
        return difflib.SequenceMatcher(None, titulo.lower(), palabra_buscada.lower()).ratio()