from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Abstractos.Error import *

import Abstractos.Globales as Errores

class Acceso(Expresion):

    def __init__(self, objeto, tipo, fila, columna, objAnterior = None):
        self.Objeto = objeto
        self.Tipo = tipo
        self.Fila = fila
        self.Columna = columna
        self.ObjAnterior = objAnterior # Si es necesario tener: este -> |id|.attr  

    def execute(self, entorno):
        
        if self.Tipo == "ID":
            # Acceso singular - id
            simbolo = entorno.getSimbolo(self.Objeto)
            if simbolo == None:
                Errores.tablaErrores.append(Error(f"No existe la variable: {self.Objeto}", self.Fila, self.Columna))
                return Retorno("ERROR", "Variable")
            return Retorno(simbolo.Valor, simbolo.Tipo)

        elif self.Tipo == "array":
            # Acceso singular - arreglo
            if not isinstance(self.Objeto.Array,list):
                objArray = entorno.getSimbolo(self.Objeto.Array)
                valorIndice = Acceso.getValorIndice(self.Objeto, objArray, entorno)
                return valorIndice
            else:
                return self.Objeto.execute(entorno)

        elif self.Tipo == "mix":
            # Obtener pila de acceso
            pilaAcceso = Acceso.getPila(self.Objeto)
            simboloActual = None

            for acceso in pilaAcceso:
                #print(acceso.Objeto)
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

            return simboloActual

    # Obtener el valor del atributo
    def getValorAttr(simbolo, id, entorno):
        objStruct = simbolo.Valor
        for attr in objStruct.Atributos:
            if attr.ID == id:
                if attr.Tipo == "ID":
                    objRef = attr.Valor.execute(entorno)
                    return Retorno(objRef.Valor, objRef.Tipo)
                else:
                    return Retorno(attr.Valor, attr.Tipo)

    def getValorIndice(array, simbolo, entorno):
        indicesAcceso = []
        for indice in array.Indices:
            exp = indice.execute(entorno)
            if exp.Valor == "ERROR" or exp.Tipo != "Int64" or exp.Valor == 0:
                Errores.tablaErrores.append(Error(f"El indice no es Int64, es 0 o antecede un error", array.Fila, array.Columna))
                return Retorno("ERROR", "indice")
            else:
                indicesAcceso.append(exp.Valor)

        valorIndice = None
        while len(indicesAcceso) > 0: # Iterar hasta completar los indices
            indiceActual = indicesAcceso[0]
            try:
                objIndice = simbolo.Valor[indiceActual-1]

                if objIndice.Tipo == "ID" or objIndice.Tipo == "array": 
                    # Pasar ref structs y arreglos, tambien funciona para array declarado adentro
                    valorIndice = objIndice.execute(entorno)
                else:
                    # Pasar valor
                    valorIndice = objIndice
                
                del indicesAcceso[0] # Borra el indice ya procesado
                simbolo = valorIndice # Nuevo valor a iterar
            except:
                Errores.tablaErrores.append(Error(f"Error al acceder al indice", self.Fila, self.Columna))
                return Retorno("ERROR", "indice")

        return Retorno(valorIndice.Valor, valorIndice.Tipo)

    def getPila(accesos):
        pila = []
        if not isinstance(accesos,list):
            pila.append(accesos)
            return pila
        for acceso in accesos:
            if acceso.Tipo == "mix":
                pila.extend(Acceso.getPila(acceso.Objeto)) 
            else:
                pila.append(acceso)
        return pila
