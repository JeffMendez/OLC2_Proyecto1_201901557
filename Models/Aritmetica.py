from Abstractos.Expresion import *
from Abstractos.Retorno import *

class Aritmetica(Expresion):

    def __init__(self, opIzq, opDer, operacion):
        self.OpIzq = opIzq
        self.OpDer = opDer
        self.Operacion = operacion

    def execute(self, entorno):
        valorIzq = self.OpIzq.execute(None)
        valorDer = None

        if self.OpDer:
            valorDer = self.OpDer.execute(None)

        resultado = Retorno(0, "int")

        if self.Operacion == "+":
            resultado.Valor = valorIzq.Valor + valorDer.Valor
        elif self.Operacion == "-":
            resultado.Valor = valorIzq.Valor - valorDer.Valor
        elif self.Operacion == "*":
            resultado.Valor = valorIzq.Valor * valorDer.Valor
        elif self.Operacion == "/":
            resultado.Valor = valorIzq.Valor / valorDer.Valor
        elif self.Operacion == "umenos":
            resultado.Valor = valorIzq.Valor * -1

        return resultado
