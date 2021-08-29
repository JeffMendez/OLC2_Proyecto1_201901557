from Abstractos.Expresion import *
from Abstractos.Retorno import *

class Asignacion(Expresion):

    def __init__(self, id, expresion, tipo):
        self.ID = id
        self.Expresion = expresion
        self.Tipo = tipo
    
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
                                if valorExp.Tipo == attrSt.Tipo or attrSt.Tipo == "Any":
                                    # Este valor se pasa por ref al simbolo
                                    attrSt.Valor = valorExp.Valor
                                    return

                        print("Error atributo no existe")
                    else:
                        print("Error struct inmutable")         
                else:
                    print("Error no se encontro")
                return

            # Para variables, arreglos - Verificar tipo si viene
            if self.Tipo != None:
                if valorExp.Tipo != self.Tipo:
                    print(f"Error: Asignacion invalida: {self.Tipo} con {valorExp.Tipo}")
                    return

            # Agregar a la tabla de simbolos
            entorno.setSimbolo(self.ID, valorExp, valorExp.Tipo)

            
                

            

