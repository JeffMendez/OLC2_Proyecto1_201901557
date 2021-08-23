from Abstractos.Expresion import *
from Abstractos.Retorno import *

class If(Expresion):

    def __init__(self, condicion, instrucciones, elseInst):
        self.Condicion = condicion
        self.Instrucciones = instrucciones
        self.ElseInst = elseInst

    def execute(self, entorno):
        valorCondicion = self.Condicion.execute(entorno)

        if valorCondicion.Tipo != "Bool":
            print("La condicion no resulta en boolean")
            return
        
        if valorCondicion.Valor:
            return self.Instrucciones.execute(entorno)
        elif self.ElseInst != None:
            return self.ElseInst.execute(entorno)
