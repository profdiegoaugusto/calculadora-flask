class Calculadora:

    @staticmethod
    def calcular(numero_1, numero_2, operacao):

        if operacao == "A":
            return numero_1 + numero_2
        elif operacao == "S":
            return numero_1 - numero_2
        elif operacao == "M":
            return numero_1 * numero_2
        elif operacao == "D":

            if numero_2 != 0:
                return numero_1 / numero_2
            else:
                return 'Erro: impossível dividir por zero!'
