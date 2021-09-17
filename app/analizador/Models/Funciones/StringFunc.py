from ...Abstractos.Expresion import *
from ...Abstractos.Retorno import *
from ...Abstractos.Error import *
from ...Abstractos import Globales

import random
import graphviz

class StringFunc(Expresion):

    def __init__(self, expresion, fila, columna):
        self.Expresion = expresion
        self.Fila = fila
        self.Columna = columna
    
    def execute(self, entorno):
        exp = self.Expresion.execute(entorno)
        stringConv = ""

        if exp.Valor == "ERROR":
            return Retorno("ERROR", "stringFunc")
        else:
            if exp.Tipo == "Nulo": stringConv += "nothing"
            elif exp.Tipo == "Bool": stringConv += "true" if (exp.Valor == True) else "false"
            elif exp.Tipo == "struct": stringConv += self.stringStruct(exp, self.Expresion, entorno)
            elif exp.Tipo == "array": stringConv += self.stringArreglo(exp, entorno)
            else: stringConv += str(exp.Valor)

        return Retorno(stringConv, "String")

    def stringStruct(self, objeto, simbolo, entorno = None):
        objStruct = objeto.Valor
        
        salida = objStruct.ID + "("

        for i, attr in enumerate(objStruct.Atributos):
            # Struct y array
            if attr.Tipo == "array": salida += self.stringArreglo(attr, entorno)
            elif attr.Tipo == "struct": salida += self.stringStruct(attr, simbolo, entorno)
            # Attr por valor
            else: salida += str(attr.Valor)

            if i < len(objStruct.Atributos) - 1: salida += ","

        salida += ")"

        return salida

    def stringArreglo(self, objeto, entorno = None):
        arreglo = objeto.Valor.Array

        salida = "["

        for i, item in enumerate(arreglo):
            
            # Struct y array
            if item.Tipo == "array": salida += self.stringArreglo(item, entorno)
            elif item.Tipo == "struct": salida += self.stringStruct(item, objeto, entorno)
            # Indice por valor
            else: salida += str(item.Valor)

            if i < len(arreglo) - 1: salida += ","

        salida += "]" 

        return salida
    
    def getAST(self, dot):
        idFuncion = str(random.randint(1, 1000000000))
        idParse = str(random.randint(1, 1000000000))
        idParIzq = str(random.randint(1, 1000000000))
        idParDer = str(random.randint(1, 1000000000))
        idExpresion = str(random.randint(1, 1000000000))

        dot.node(idFuncion, "funcion")
        dot.node(idParse, "string")
        dot.node(idParIzq, "(")
        dot.node(idExpresion, "expresion")
        dot.node(idParDer, ")")
      
        dot.edge(idFuncion, idParse)
        dot.edge(idFuncion, idParIzq)
        dot.edge(idFuncion, idExpresion)
        dot.edge(idFuncion, idParDer)

        dot, IDDotExp = self.Expresion.getAST(dot)
        dot.edge(idExpresion, IDDotExp)

        return dot, idFuncion