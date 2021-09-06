from Abstractos.Expresion import *
import Abstractos.Globales as Globales

class Print(Expresion):

    # PENDIENTE ARREGLO DE SALIDAS NUEVA LINEA
    
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
            if attr.Tipo == "ID":
                # Attr por ref
                item = attr.Valor
                objetoRef = item.execute(entorno)

                if objetoRef.Tipo == "array": salida += Print.printArreglo(objetoRef, entorno)
                elif objetoRef.Tipo == "struct": salida += Print.printStruct(objetoRef, attr.Valor, entorno)
            
            else:
                # Array declarado dentro
                if attr.Tipo == "array": salida += Print.printArreglo(attr,entorno)
                # Attr por valor
                else: salida += str(attr.Valor)

            if i < len(objStruct.Atributos) - 1: salida += ","

        salida += ")"

        return salida

    def printArreglo(objeto, entorno = None):
        salida = "["

        for i, item in enumerate(objeto.Valor):
            
            if item.Tipo == "ID":
                # Item por ref
                objetoRef = item.execute(entorno)
                if objetoRef.Tipo == "array": salida += Print.printArreglo(objetoRef, entorno)
                elif objetoRef.Tipo == "struct": salida += Print.printStruct(objetoRef, item, entorno)
            else:
                # Array declarado dentro
                if item.Tipo == "array": 
                    arrayValue = item.execute(entorno)
                    salida += Print.printArreglo(arrayValue,entorno)
                    
                # Item por valor
                else: salida += str(item.Valor)

            if i < len(objeto.Valor) - 1: salida += ","

        salida += "]" 

        return salida


       
        