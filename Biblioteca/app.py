from flask import Flask, render_template, request, redirect, url_for
from buscador import Buscador

app = Flask(__name__)

class Inicio:
    # Redirigir la raíz a /FragaCultural/
    @app.route('/')
    def root_redirect():
        return redirect(url_for('inicio'))

    # Ruta principal para FragaCultural
    @app.route('/FragaCultural/', methods=['GET', 'POST'])
    def inicio():
        books = []  # Inicializar books como lista vacía
        if request.method == 'POST':
            # obtengo el titulo ingresado por el usuario
            search_query = request.form.get('search_query')
            b = Buscador()
            books = b.busca_google_books(search_query)
        return render_template('index.html', books=books)
    
if __name__ == "__main__":
    app.run(debug=True, port=5000, use_reloader=False)
