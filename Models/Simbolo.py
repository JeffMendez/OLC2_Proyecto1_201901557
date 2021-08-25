from Abstractos.Expresion import *
from Abstractos.Retorno import *

class Simbolo(Expresion):

    # Tipo -> int, string, etc
    # Clase -> variable, arreglo, struct

    def __init__(self, valor, tipo, id):
        self.Valor = valor
        self.Tipo = tipo
        self.ID = id

    def execute(self, entorno):

        if self.Tipo == "ID":
            simbolo = entorno.getSimbolo(self.ID)
            if simbolo == None:
                print(f"Error: Acceso invalido: no existe la variable")
                return Retorno("ERROR", "Variable")
            return Retorno(simbolo.Valor, simbolo.Tipo)
        
        elif self.Tipo == "struct":
            simbolo = entorno.getSimbolo(self.ID)
            if simbolo == None:
                print(f"Error: Acceso invalido: no existe el struct")
                return Retorno("ERROR", "Struct")
            
            objStruct = simbolo.Valor
            for attr in objStruct.Atributos:
                if attr.ID == self.Valor:
                    return Retorno(attr.Valor, attr.Tipo)
            
            print(f"Error: Atributo no existe")
            return Retorno("ERROR", "Atributo")

        return Retorno(self.Valor, self.Tipo)

