from ...Abstractos.Expresion import *
from ...Abstractos.Retorno import *
from ...Abstractos.Error import *

import random
import graphviz

class Funcion(Expresion):

    def __init__(self, idFuncion, parametros, instrucciones, fila, columna):
        self.IDFuncion = idFuncion
        self.Parametros = parametros
        self.Instrucciones = instrucciones
        self.Fila = fila
        self.Columna = columna

    def execute(self, entorno):
        entorno.setFuncion(self.IDFuncion, self, self.Fila, self.Columna)

    def getAST(self, dot):
        idDecl = str(random.randint(1, 1000000000))
        idFunction = str(random.randint(1, 1000000000))
        idVariable = str(random.randint(1, 1000000000))
        idParIzq = str(random.randint(1, 1000000000))
        idParametros = str(random.randint(1, 1000000000))
        idParDer = str(random.randint(1, 1000000000))
        idBloque = str(random.randint(1, 1000000000))
        idEnd = str(random.randint(1, 1000000000))

        dot.node(idDecl, "declaracion")
        dot.node(idFunction, "funcion")
        dot.node(idVariable, self.IDFuncion)
        dot.node(idParIzq, "(")

        dot.edge(idDecl, idFunction)
        dot.edge(idDecl, idVariable)
        dot.edge(idDecl, idParIzq)
        

        # Parametros
        if self.Parametros:
            dot.node(idParametros, "parametros")
            dot.edge(idDecl, idParametros)
            for i, param in enumerate(self.Parametros):
                dot, IDDotParam = param.getAST(dot)
                dot.edge(idParametros, IDDotParam)

                if i < len(self.Parametros) - 1:
                    idComa = str(random.randint(1, 1000000000))
                    dot.node(idComa, ",")
                    dot.edge(idParametros, idComa)
            
        dot.node(idParDer, ")")
        dot.edge(idDecl, idParDer)

        # Bloque
        dot.node(idBloque, "bloque")
        dot.edge(idDecl, idBloque)
        dot, IDDotBloque = self.Instrucciones.getAST(dot)
        dot.edge(idBloque, IDDotBloque)

        dot.node(idEnd, "end;")
        dot.edge(idDecl, idEnd)

        return dot, idDecl

        