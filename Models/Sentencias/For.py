from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Abstractos.Error import *
from Models.Entorno import *

import Abstractos.Globales as Errores

class For(Expresion):

    def __init__(self, variable, expresion, instrucciones, fila, columna):
        self.Variable = variable
        self.Expresion = expresion
        self.Instrucciones = instrucciones
        self.Fila = fila
        self.Columna = columna
    
    def execute(self, entorno):
        valorExp = self.Expresion.execute(entorno)
    
        # Validacion iterador
        if valorExp.Tipo != "Rango" and valorExp.Tipo != "String" and valorExp.Tipo != "array":
            Errores.tablaErrores.append(Error(f"La expresion del for no es valida: {valorExp.Tipo}", self.Fila, self.Columna))
            return
        
        # Para string
        if valorExp.Tipo == "String":
            # Declarar objeto
            indice = 0
            letra = Retorno(valorExp.Valor[indice], valorExp.Tipo)
            entornoFor = Entorno(entorno, "")
            entornoFor.setSimbolo(self.Variable, letra, letra.Tipo)
            
            while True:
                resultCorrida = self.Instrucciones.execute(entornoFor)
                
                # Sentencias de transferencia
                if resultCorrida != None:
                    if resultCorrida.Tipo == "continue":
                        # Actualizar iterador
                        iterador = entornoFor.getSimbolo(self.Variable)
                        if indice < len(valorExp.Valor)-1:
                            indice = indice + 1
                            iterador.Valor = valorExp.Valor[indice]
                        else: return
                        continue
                    elif resultCorrida.Tipo == "break":
                        return
                    elif resultCorrida.Tipo == "return":
                        return resultCorrida
                        
                # Actualizar iterador
                iterador = entornoFor.getSimbolo(self.Variable)
                if indice < len(valorExp.Valor)-1:
                    indice = indice + 1
                    iterador.Valor = valorExp.Valor[indice]
                else:
                    return
        
        # Para arreglo
        if valorExp.Tipo == "array":
            # Declarar objeto
            indice = 0
            item = valorExp.Valor[indice]
            entornoFor = Entorno(entorno, "")
            entornoFor.setSimbolo(self.Variable, item, item.Tipo)
            
            while True:
                resultCorrida = self.Instrucciones.execute(entornoFor)

                # Sentencias de transferencia
                if resultCorrida != None:
                    if resultCorrida.Tipo == "continue":
                        # Actualizar iterador
                        iterador = entornoFor.getSimbolo(self.Variable)
                        if indice < len(valorExp.Valor)-1:
                            indice = indice + 1
                            iterador = valorExp.Valor[indice]
                            entornoFor.setSimbolo(self.Variable, iterador, iterador.Tipo)          
                        else: return
                        continue
                    elif resultCorrida.Tipo == "break":
                        return
                    elif resultCorrida.Tipo == "return":
                        return resultCorrida

                # Actualizar iterador
                iterador = entornoFor.getSimbolo(self.Variable)
                if indice < len(valorExp.Valor)-1:
                    indice = indice + 1
                    iterador = valorExp.Valor[indice]
                    entornoFor.setSimbolo(self.Variable, iterador, iterador.Tipo)          
                else:
                    return
            
        # Para rango
        if valorExp.Tipo == "Rango":
            inicio = valorExp.Valor[0]
            fin = valorExp.Valor[1]

            # Validacion palabras reservadas
            if inicio == 'begin' or inicio == 'end' or fin == 'begin' or fin == 'end' :
                Errores.tablaErrores.append(Error(f"Rango sin arreglo no acepta begin-end", self.Fila, self.Columna))
                return

            inicio = inicio.execute(entorno)
            fin = fin.execute(entorno)

            # Validacion tipos int
            if inicio.Tipo != "Int64" or fin.Tipo != "Int64":
                Errores.tablaErrores.append(Error(f"Rango solo acepta Int64", self.Fila, self.Columna))
                return
            elif fin.Valor < inicio.Valor:
                Errores.tablaErrores.append(Error(f"For unicamente ascendente", self.Fila, self.Columna))
                return
            
            entornoFor = Entorno(entorno, "")
            entornoFor.setSimbolo(self.Variable, inicio, inicio.Tipo)

            while True:    
                resultCorrida = self.Instrucciones.execute(entornoFor)

                # Sentencias de transferencia
                if resultCorrida != None:
                    if resultCorrida.Tipo == "continue":
                        # Actualizar iterador
                        iterador = entornoFor.getSimbolo(self.Variable)
                        if iterador.Valor < fin.Valor:
                            iterador.Valor = iterador.Valor + 1
                        else: return
                        continue
                    elif resultCorrida.Tipo == "break":
                        return
                    elif resultCorrida.Tipo == "return":
                        return resultCorrida

                # Actualizar iterador
                iterador = entornoFor.getSimbolo(self.Variable)
                if iterador.Valor < fin.Valor:
                    iterador.Valor = iterador.Valor + 1
                else:
                    return

                
