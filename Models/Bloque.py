
from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Models.Entorno import *

class Bloque(Expresion):

    def __init__(self, instrucciones):
        self.Instrucciones = instrucciones
   
    def execute(self, entorno):
        nuevoEntorno = Entorno(entorno, "")
        for inst in self.Instrucciones:
            retornoInst = inst.execute(nuevoEntorno)
            if retornoInst != None:
                return retornoInst