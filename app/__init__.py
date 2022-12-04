from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Vamos River"

def pagina_no_encontrada(error):
    return render_template('/404.html')


def inicializar_app(config):
    app.config.from_object(config)
    return app
