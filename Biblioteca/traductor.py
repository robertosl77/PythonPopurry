# pip install googletrans==4.0.0-rc1

from googletrans import Translator

class Traductor:
    def __init__(self):
        self.translator = Translator()

    def traducir_al_espanol(self, texto):
        if texto==None:
            return None
        # Detectar el idioma de origen
        deteccion = self.translator.detect(texto)
        idioma_origen = deteccion.lang
        if idioma_origen=='es':
            return texto
        # Traducir al español
        traduccion = self.translator.translate(texto, dest='es')
        try:
            return f"{traduccion.text}"
        except Exception as e:
            return texto
        

# Ejemplo de uso
# traductor = Traductor()
# resultado = traductor.traducir_al_espanol("Hello, how are you?")
# print(resultado)
