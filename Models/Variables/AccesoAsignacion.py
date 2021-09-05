from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Abstractos.Error import *
from Models.Variables.Acceso import *

import Abstractos.Globales as Errores

class AccesoAsignacion(Expresion):

    def __init__(self, acceso, expresion, tipo, fila, columna):
        self.AccesoSimbolo = acceso
        self.Expresion = expresion
        self.Tipo = tipo
        self.Fila = fila
        self.Columna = columna

    def execute(self, entorno):
        valorExp = self.Expresion.execute(entorno)
        if valorExp.Valor != "ERROR":
            if self.AccesoSimbolo.Tipo == "mix":
                
                pilaAcceso = Acceso.getPila(self.AccesoSimbolo.Objeto)
                simboloActual = None
                simboloAnterior = None

                for i, acceso in enumerate(pilaAcceso):
                    if i == len(pilaAcceso) - 1:
                        # Cambiar el valor objetivo
                        # attr.id
                        if simboloActual.Tipo == "struct" and type(acceso.Objeto) == str:
                            AccesoAsignacion.setValorAttr(simboloActual, acceso.Objeto, self.Tipo, valorExp)
                        # attr.id[]
                        if simboloActual.Tipo == "struct" and acceso.Tipo == "array":
                            idAttr = acceso.Objeto.Array
                            atributo = Acceso.getValorAttr(simboloActual, idAttr, entorno)
                            AccesoAsignacion.setValorIndice(acceso.Objeto, atributo, valorExp, self.Tipo, entorno)
                        return
                    else:
                        # Acceder a los objetos
                        if simboloActual == None:
                            # Primer ID o arreglo
                            simboloActual = acceso.execute(entorno)
                        else:
                            # Caso obj.attributo
                            if simboloActual.Tipo == "struct" and type(acceso.Objeto) == str:
                                simboloActual = Acceso.getValorAttr(simboloActual, acceso.Objeto, entorno)       
                            # Caso obj.array[1]
                            if simboloActual.Tipo == "struct" and acceso.Tipo == "array":
                                idAttr = acceso.Objeto.Array
                                atributo = Acceso.getValorAttr(simboloActual, idAttr, entorno)
                                valorIndice = Acceso.getValorIndice(acceso.Objeto, atributo, entorno)
                                simboloActual = valorIndice

            else:
                # Acceso simple array[][][]
                arrayObj = self.AccesoSimbolo.Objeto
                simboloArray = entorno.getSimbolo(arrayObj.Array)
                AccesoAsignacion.setValorIndice(arrayObj, simboloArray, valorExp, self.Tipo, entorno)
        
    def setValorAttr(simbolo, id, tipo, expresion):
        objStruct = simbolo.Valor
        for attr in objStruct.Atributos:
            if attr.ID == id:
                # Se cambia por referencia
                attr.Valor = expresion.Valor
                attr.Tipo = expresion.Tipo

    def setValorIndice(array, simbolo, expresion, tipo, entorno):
        indicesAcceso = []
        for indice in array.Indices:
            exp = indice.execute(entorno)
            if exp.Valor == "ERROR" or exp.Tipo != "Int64" or exp.Valor == 0:
                Errores.tablaErrores.append(Error(f"El indice no es Int64, es 0 o antecede un error", array.Fila, array.Columna))
                return Retorno("ERROR", "indice")
            else:
                indicesAcceso.append(exp.Valor)

        valorIndice = None
        accesoAnterior = None

        while len(indicesAcceso) > 0: # Iterar hasta completar los indices
            indiceActual = indicesAcceso[0]
            try:

                if len(indicesAcceso) == 1:
                    # Ultimo indice hacer cambio
                    #entorno.setSimbolo(self.ID, valorExp, valorExp.Tipo)
                    #print(accesoAnterior, simbolo.Valor)
                    simbolo.Valor[indiceActual-1].Valor = expresion.Valor
                    simbolo.Valor[indiceActual-1].Tipo = expresion.Tipo
                    return
                    
                objIndice = simbolo.Valor[indiceActual-1]
                if objIndice.Tipo == "ID" or objIndice.Tipo == "array": 
                    # Pasar ref structs y arreglos, tambien funciona para array declarado adentro
                    valorIndice = objIndice.execute(entorno)
                else:
                    # Pasar valor
                    valorIndice = objIndice
                del indicesAcceso[0] # Borra el indice ya procesado
                accesoAnterior = simbolo
                simbolo = valorIndice # Nuevo valor a iterar
            except:
                Errores.tablaErrores.append(Error(f"Error al acceder al indice", array.Fila, array.Columna))
                return Retorno("ERROR", "indice")


