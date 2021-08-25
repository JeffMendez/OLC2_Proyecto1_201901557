from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Models.Entorno import *
from Models.Variables.Struct import *

class Llamada(Expresion):

    def __init__(self, id, params):
        self.ID = id
        self.Params = params
    
    def execute(self, entorno):
        llamada = entorno.getSimbolo(self.ID)

        if llamada != None:
            # Para structs
            if llamada.Tipo == "struct":
                structBase = llamada.Valor
                objeto = Struct("", structBase.Mutable, structBase.Atributos)
                
                for i in range(len(self.Params)):
                    valorParam = self.Params[i].execute(entorno)

                    if objeto.Atributos[i].Tipo == "Any" or valorParam.Tipo == objeto.Atributos[i].Tipo:
                        objeto.Atributos[i].Valor = valorParam.Valor
                        objeto.Atributos[i].Tipo = valorParam.Tipo
                    else:
                        print("dato incorrecto")
                        return Retorno("ERROR", "struct")

                return Retorno(objeto, "struct")
        else:
            print("No existe")