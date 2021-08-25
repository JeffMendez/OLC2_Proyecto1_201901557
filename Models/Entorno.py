from Models.Simbolo import *

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
    def setStruct(self, id, struct):
        nuevoStruct = Simbolo(struct, "struct", id)

        entorno = self
        # Verificar que no exista
        while entorno != None:
            if id in entorno.TablaSimbolos.keys():
                print("Struct repetido")
                return
            entorno = entorno.Padre
        # Setear si no esta agregado
        self.TablaSimbolos[id] = nuevoStruct

    def getSimbolo(self, id):
        entorno = self
        while entorno != None:
            if id in entorno.TablaSimbolos.keys():
                return entorno.TablaSimbolos[id]
            entorno = entorno.Padre
        return None
    

