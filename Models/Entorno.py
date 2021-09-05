from Models.Simbolo import *
from Abstractos.Error import *

import Abstractos.Globales as Errores

class Entorno:

    def __init__(self, padre, nombre):
        self.Padre = padre
        self.Nombre = nombre
        self.TablaSimbolos = {}
        self.PilaSentencias = {} # Controlar break, continue
        self.PilaFunciones = {} # Controlar funciones, metodos

    # Para variables normales
    def setSimbolo(self, id, exp, tipo):
        nuevoSimbolo = Simbolo(exp.Valor, tipo, id)

        entorno = self
        # Actualizar si ya existe
        while entorno != None:
            if id in entorno.TablaSimbolos.keys():
                entorno.TablaSimbolos[id] = nuevoSimbolo
                return
            entorno = entorno.Padre
        # Setear si no esta agregado
        self.TablaSimbolos[id] = nuevoSimbolo
    
    # Para structs
    def setStruct(self, id, struct, fila, columna):
        nuevoStruct = Simbolo(struct, "struct", id)

        entorno = self
        # Verificar que no exista
        while entorno != None:
            if id in entorno.TablaSimbolos.keys():
                Errores.tablaErrores.append(Error(f"Struct ya declarado: {id}", fila, columna))
                return
            entorno = entorno.Padre
        # Setear si no esta agregado
        self.TablaSimbolos[id] = nuevoStruct

    def setFuncion(self, id, funcion, fila, columna):
        nuevaFuncion = Simbolo(funcion, "funcion", id)

        entorno = self
        # Verificar que no exista
        while entorno != None:
            if id in entorno.TablaSimbolos.keys():
                Errores.tablaErrores.append(Error(f"Funcion ya declarada: {id}", fila, columna))
                return
            entorno = entorno.Padre
        # Setear si no esta agregado
        self.TablaSimbolos[id] = nuevaFuncion

    def getSimbolo(self, id):
        entorno = self
        while entorno != None:
            if id in entorno.TablaSimbolos.keys():
                return entorno.TablaSimbolos[id]
            entorno = entorno.Padre
        return None
    

