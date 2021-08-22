from Models.Simbolo import *

class Entorno:

    def __init__(self, padre, nombre):
        self.Padre = padre
        self.Nombre = nombre
        self.TablaSimbolos = {}
        self.PilaSentencias = {} # Controlar break, continue
        self.PilaFunciones = {} # Controlar funciones, metodos

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
    
    def getSimbolo(self, id):
        entorno = self
        while entorno != None:
            if id in entorno.TablaSimbolos.keys():
                return entorno.TablaSimbolos[id]
            entorno = entorno.Padre
        return None
        
