from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Abstractos.Error import *

from Models.Entorno import *
from Models.Variables.Struct import *

import Abstractos.Globales as Errores

from copy import copy, deepcopy

class Llamada(Expresion):

    def __init__(self, id, params, fila, columna):
        self.ID = id
        self.Params = params
        self.Fila = fila
        self.Columna = columna
    
    def execute(self, entorno):
        llamada = entorno.getSimbolo(self.ID)

        if llamada != None:

            # Para structs
            if llamada.Tipo == "struct":
                structBase = llamada.Valor
                objeto = Struct(self.ID, structBase.Mutable, deepcopy(structBase.Atributos))
                
                for i in range(len(self.Params)):
                    valorParam = self.Params[i].execute(entorno)

                    if objeto.Atributos[i].Tipo == "Any" or valorParam.Tipo == objeto.Atributos[i].Tipo or objeto.Atributos[i].TipoOrigen == "Any":
                        
                        if valorParam.Tipo == "struct":
                            # Para valores referencias
                            objeto.Atributos[i].Valor = self.Params[i]
                            objeto.Atributos[i].Tipo = "ID"

                        elif valorParam.Tipo == "array":

                            if hasattr(self.Params[i], 'Array'):
                                # Declaracion
                                objeto.Atributos[i].Valor = valorParam.Valor
                                objeto.Atributos[i].Tipo = valorParam.Tipo
                            else:
                                # Referencia
                                objeto.Atributos[i].Valor = self.Params[i]
                                objeto.Atributos[i].Tipo = "ID"

                        else:
                            # Variables normales
                            objeto.Atributos[i].Valor = valorParam.Valor
                            objeto.Atributos[i].Tipo = valorParam.Tipo

                    else:
                        Errores.tablaErrores.append(Error(f"El tipo del atributo no coincide: {objeto.Atributos[i].ID} con {valorParam.Tipo}", self.Fila, self.Columna))
                        return Retorno("ERROR", "struct")

                return Retorno(objeto, "struct")

            # Para funciones
            elif llamada.Tipo == "funcion":
                objFuncion = llamada.Valor

                if self.Params == None and objFuncion.Parametros == None:
                    objFuncion.Instrucciones.execute(entorno)
                    if resultado == None: return Retorno(None, "Nulo")
                    else:
                        print("se beria retornar algo")
                        return
                else:
                    if self.Params == None or objFuncion.Parametros == None or len(self.Params) != len(objFuncion.Parametros):
                        Errores.tablaErrores.append(Error(f"Parametros no coinciden", self.Fila, self.Columna))
                        return Retorno("ERROR", "indice")
                    else:      

                        entornoFuncion = Entorno(entorno, "")
                        indiceParam = 0

                        for paramExp in self.Params:
                            exp = paramExp.execute(entorno)
       
                            if exp.Tipo == "struct" or exp.Tipo == "array":
                                # Pasar ref
                                # struct
                                if exp.Tipo == "struct":
                                    paramFuncion = objFuncion.Parametros[indiceParam]
                                    if exp.Valor.ID == paramFuncion.IDTipo or paramFuncion.IDTipo == "Any":
                                        entornoFuncion.setSimbolo(paramFuncion.IDParam, exp, "struct")
                                        indiceParam += 1
                                    else:
                                        Errores.tablaErrores.append(Error(f"Tipos no coinciden", self.Fila, self.Columna))
                                        return Retorno("ERROR", "indice")
                                # array
                                elif exp.Tipo == "array":
                                    paramFuncion = objFuncion.Parametros[indiceParam]
                                    if paramFuncion.IDTipo == "Any":
                                        entornoFuncion.setSimbolo(paramFuncion.IDParam, exp, "array")
                                        indiceParam += 1
                                    else:
                                        Errores.tablaErrores.append(Error(f"Tipos no coinciden", self.Fila, self.Columna))
                                        return Retorno("ERROR", "indice")

                            else:
                                # Pasar valor
                                paramFuncion = objFuncion.Parametros[indiceParam]
                                if paramFuncion.IDTipo == exp.Tipo or paramFuncion.IDTipo == "Any":
                                    entornoFuncion.setSimbolo(paramFuncion.IDParam, exp, exp.Tipo)
                                    indiceParam += 1
                                else:
                                    Errores.tablaErrores.append(Error(f"Tipos no coinciden", self.Fila, self.Columna))
                                    return Retorno("ERROR", "indice")

                        # Ejecutar bloque funcion
                        resultado = objFuncion.Instrucciones.execute(entornoFuncion)
                        if resultado == None: return Retorno(None, "Nulo")
                        else:
                            print("se beria retornar algo")
                            
                
        else:
            Errores.tablaErrores.append(Error(f"La funcion o struct no existe: {self.ID}", self.Fila, self.Columna))
            return Retorno("ERROR", "llamada")
