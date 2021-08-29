from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Abstractos.Error import *

import Abstractos.Globales as Errores

class Asignacion(Expresion):

    def __init__(self, id, expresion, tipo, fila, columna):
        self.ID = id
        self.Expresion = expresion
        self.Tipo = tipo
        self.Fila = fila
        self.Columna = columna
    
    def execute(self, entorno):
        valorExp = self.Expresion.execute(entorno)

        if valorExp.Valor != "ERROR":

            # Para structs
            if self.Tipo == "struct":
                idStruct = self.ID[0]
                attr = self.ID[1]

                simbolo = entorno.getSimbolo(idStruct)
                
                if simbolo != None:
                    objStruct = simbolo.Valor
                    if objStruct.Mutable:
                        for attrSt in objStruct.Atributos:
                            if attrSt.ID == attr:
                                if attrSt.TipoOrigen == "Any" or valorExp.Tipo == attrSt.Tipo:
                                    # Este valor se pasa por ref al simbolo
                                    attrSt.Valor = valorExp.Valor
                                    attrSt.Tipo = valorExp.Tipo
                                else:
                                    # Tipo no coincide
                                    Errores.tablaErrores.append(Error(f"El tipo del atributo no coincide: {attrSt.ID} con {valorExp.Tipo}", self.Fila, self.Columna))
                                return
                        # Attr no existe
                        Errores.tablaErrores.append(Error(f"El atributo no existe: {attr}", self.Fila, self.Columna))
                        return
                    else:
                        # Inmutable
                        Errores.tablaErrores.append(Error(f"Struct {idStruct} inmutable, cambio rechazado", self.Fila, self.Columna))
                        return         
                else:
                    # No Existe
                    Errores.tablaErrores.append(Error(f"El objeto struct {idStruct} no existe", self.Fila, self.Columna))
                return

            # Para variables, arreglos - Verificar tipo si viene
            if self.Tipo != None:
                if valorExp.Tipo != self.Tipo:
                    Errores.tablaErrores.append(Error(f"Asignacion invalida: {self.Tipo} con {valorExp.Tipo}", self.Fila, self.Columna))
                    return

            # Agregar a la tabla de simbolos
            entorno.setSimbolo(self.ID, valorExp, valorExp.Tipo)

            
                

            

