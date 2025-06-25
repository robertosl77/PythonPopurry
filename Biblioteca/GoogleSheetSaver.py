import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetSaver:
    def __init__(self, sheet_name, worksheet_name):
        # Autenticación con Google Sheets API
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        client = gspread.authorize(creds)
        
        # Abrir el archivo y seleccionar la hoja
        self.sheet = client.open(sheet_name).worksheet(worksheet_name)

    def guardar_datos(self, data):
        """
        Guarda los datos de un JSON en la Google Sheet.
        data: JSON con los datos a guardar (debe ser una lista de diccionarios).
        """
        headers = list(data[0].keys())  # Los encabezados serán las claves del JSON
        valores = [list(item.values()) for item in data]

        # Insertar encabezados en la primera fila si no están ya
        if not self.sheet.get_all_values():
            self.sheet.insert_row(headers, 1)

        # Insertar los valores a partir de la segunda fila
        for valor in valores:
            self.sheet.append_row(valor)

# Ejemplo de uso
# if __name__ == "__main__":
#     datos = [
#         {
#             "titulo": "Libro 1",
#             "autor": "Autor 1",
#             "publicacion_año": "2024",
#             "isbn13": "978-3-16-148410-0",
#             "isbn10": "3-16-148410-X"
#         },
#         {
#             "titulo": "Libro 2",
#             "autor": "Autor 2",
#             "publicacion_año": "2023",
#             "isbn13": "978-1-23-456789-0",
#             "isbn10": "1-23-456789-X"
#         }
#     ]

#     google_sheet = GoogleSheetSaver("Nombre_de_Tu_Spreadsheet", "Hoja1")
#     google_sheet.guardar_datos(datos)
