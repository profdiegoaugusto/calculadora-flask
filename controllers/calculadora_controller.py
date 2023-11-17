from flask import Blueprint, render_template, request

from models.calculadora import Calculadora


class CalculadoraController:

    calculadoraBlueprint = Blueprint('calculadora', __name__, url_prefix='/calculadora')

    @calculadoraBlueprint.route("/", methods=["GET"])
    def index():
        return render_template('/calculadora/index.html')

    @calculadoraBlueprint.route("/", methods=["POST"])
    def calcular():

        numero_1 = float(request.form['numero-1'])
        numero_2 = float(request.form['numero-2'])
        operacao = request.form.get('operacao')

        resultado = Calculadora.calcular(numero_1, numero_2, operacao)

        return render_template('/calculadora/index.html', numero_1=numero_1, numero_2=numero_2, operacao=operacao, resultado=resultado)
