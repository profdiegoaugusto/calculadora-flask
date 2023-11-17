from flask import Flask

from controllers.calculadora_controller import CalculadoraController

app = Flask(__name__, template_folder="views/templates")

app.register_blueprint(CalculadoraController.calculadoraBlueprint)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
