from ...Abstractos.Expresion import *
from ...Abstractos import Globales

import random
import graphviz

class Print(Expresion):

    def __init__(self, expresion, tipo):
        self.Expresiones = expresion
        self.Tipo = tipo
    
    def execute(self, entorno):

        salida = ""
        error = False
        
        for exp in self.Expresiones:            
            valorExp = exp.execute(entorno)
            if valorExp.Valor == "ERROR":
                error = True
                break
            else:
                if valorExp.Tipo == "Nulo": salida += "nothing"
                elif valorExp.Tipo == "Bool": salida += "true" if (valorExp.Valor == True) else "false"
                elif valorExp.Tipo == "struct": salida += Print.printStruct(valorExp, exp, entorno)
                elif valorExp.Tipo == "array": salida += Print.printArreglo(valorExp, entorno)                
                else: salida += str(valorExp.Valor)
    
        if not error:
            if self.Tipo == "nl": 
                # Nueva linea
                #print(salida)
                Globales.salidaPrints += salida + "\n"  
            else:
                # Misma linea
                #print(salida, end="")
                Globales.salidaPrints += salida
               
    def printStruct(objeto, simbolo, entorno = None):
        objStruct = objeto.Valor
        
        salida = objStruct.ID + "("

        for i, attr in enumerate(objStruct.Atributos):
            # Struct y array
            if attr.Tipo == "array": salida += Print.printArreglo(attr, entorno)
            elif attr.Tipo == "struct": salida += Print.printStruct(attr, simbolo, entorno)
            # Attr por valor
            else: salida += str(attr.Valor)

            if i < len(objStruct.Atributos) - 1: salida += ","

        salida += ")"

        return salida

    def printArreglo(objeto, entorno = None):
        arreglo = objeto.Valor.Array

        salida = "["
        
        for i, item in enumerate(arreglo):
            # Struct y array
            if item.Tipo == "array": salida += Print.printArreglo(item, entorno)
            elif item.Tipo == "struct": salida += Print.printStruct(item, objeto, entorno)
            # Indice por valor
            else: salida += str(item.Valor)

            if i < len(arreglo) - 1: salida += ","
 
        salida += "]" 

        return salida

    def getAST(self, dot):
        idFuncion = str(random.randint(1, 1000000000))
        idPrint = str(random.randint(1, 1000000000))
        idParIzq = str(random.randint(1, 1000000000))
        idParDer = str(random.randint(1, 1000000000))
        idExpresiones = str(random.randint(1, 1000000000))
        idPtComa = str(random.randint(1, 1000000000))

        dot.node(idFuncion, "funcion")
        dot.node(idPrint, "println" if self.Tipo == "nl" else "print")
        dot.node(idParIzq, "(")
        dot.node(idExpresiones, "expresiones")
        dot.node(idParDer, ")")
        dot.node(idPtComa, ";")
        
        dot.edge(idFuncion, idPrint)
        dot.edge(idFuncion, idParIzq)
        dot.edge(idFuncion, idExpresiones)

        for exp in self.Expresiones:
            idExp = str(random.randint(1, 1000000000))
            dot.node(idExp, "expresion")
            dot.edge(idExpresiones, idExp)

            dot, IDDotExp = exp.getAST(dot)
            dot.edge(idExp, IDDotExp)

        dot.edge(idFuncion, idParDer)
        dot.edge(idFuncion, idPtComa)
        
        return dot, idFuncion
       
        