class Bandera:
    # Mapping of language codes to country codes for flag lookup
    language_to_country = {
        'es': 'es',  # Spanish -> Spain
        'en': 'gb',  # English -> United Kingdom
        'fr': 'fr',  # French -> France
        'de': 'de',  # German -> Germany
        # Add more languages as needed
    }

    # URL template for fetching flag icons
    flag_api_url = "https://countryflagsapi.com/png/{}"

    def obtener_url_bandera(self, idioma):
        """
        Recibe un idioma ('es', 'en', etc.) y devuelve la URL de la bandera correspondiente en formato icono.

        :param idioma: Código del idioma (es, en, fr, etc.)
        :return: URL de la bandera en formato PNG
        """
        # Convert language code to country code
        codigo_pais = self.language_to_country.get(idioma, 'un')  # 'un' is the default for unknown languages
        # Return the complete URL
        return self.flag_api_url.format(codigo_pais)


# Ejemplo de uso
# bandera = Bandera()
# url_bandera = bandera.obtener_url_bandera('es')
# print(f"URL de la bandera para 'es': {url_bandera}")
