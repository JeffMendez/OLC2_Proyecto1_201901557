from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Abstractos.Error import *

from Models.Entorno import *
from Models.Variables.Struct import *

import Abstractos.Globales as Errores

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
                objeto = Struct("", structBase.Mutable, structBase.Atributos)
                
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
        else:
            Errores.tablaErrores.append(Error(f"La funcion o struct no existe: {self.ID}", self.Fila, self.Columna))
            return Retorno("ERROR", "llamada")
