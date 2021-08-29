from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Abstractos.Error import *

import Abstractos.Globales as Errores

class Simbolo(Expresion):

    # Tipo -> int, string, etc
    # Clase -> variable, arreglo, struct

    def __init__(self, valor, tipo, id, fila = None, columna = None):
        self.Valor = valor
        self.Tipo = tipo
        self.ID = id
        self.Fila = fila
        self.Columna = columna

    def execute(self, entorno):

        if self.Tipo == "ID":
            simbolo = entorno.getSimbolo(self.ID)
            if simbolo == None:
                Errores.tablaErrores.append(Error(f"No existe la variable: {self.ID}", self.Fila, self.Columna))
                return Retorno("ERROR", "Variable")
            return Retorno(simbolo.Valor, simbolo.Tipo)
        
        elif self.Tipo == "struct":
            simbolo = entorno.getSimbolo(self.ID)
            if simbolo == None:
                Errores.tablaErrores.append(Error(f"No existe el struct: {self.ID}", self.Fila, self.Columna))
                return Retorno("ERROR", "Struct")
            
            objStruct = simbolo.Valor
            for attr in objStruct.Atributos:
                if attr.ID == self.Valor:
                    return Retorno(attr.Valor, attr.Tipo)
            
            Errores.tablaErrores.append(Error(f"Atributo no existe", self.Fila, self.Columna))
            return Retorno("ERROR", "Atributo")

        return Retorno(self.Valor, self.Tipo)

