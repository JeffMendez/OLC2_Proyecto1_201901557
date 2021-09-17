from ...Abstractos.Expresion import *
from ...Abstractos.Retorno import *
from ...Abstractos.Error import *
from ...Abstractos import Globales

import random
import graphviz

class Trunc(Expresion):

    def __init__(self, tipoConv, expresion, fila, columna):
        self.TipoConversion = tipoConv
        self.Expresion = expresion
        self.Fila = fila
        self.Columna = columna
    
    def execute(self, entorno):
        exp = self.Expresion.execute(entorno)

        if exp.Valor != "ERROR":
            if exp.Tipo == "Float64": 
                try:
                    if self.TipoConversion == "Int64":
                        return Retorno(int(exp.Valor), "Int64")
                    else:
                        Globales.tablaErrores.append(Error(f"El tipo {self.TipoConversion} no es permitido en Trunc, solo Int64", self.Fila, self.Columna))
                        return Retorno("ERROR", "Trunc")
                except:
                    Globales.tablaErrores.append(Error(f"Realizar trunc no es posible, el valor no es correcto", self.Fila, self.Columna))
                    return Retorno("ERROR", "Trunc")
            else:
                Globales.tablaErrores.append(Error(f"El tipo de la expresion {exp.Tipo} no es permitido en Trunc, solo Float64", self.Fila, self.Columna))
                return Retorno("ERROR", "Trunc")
        else:
            return Retorno("ERROR", "Trunc")

    def getAST(self, dot):
        idFuncion = str(random.randint(1, 1000000000))
        idTrunc = str(random.randint(1, 1000000000))
        idParIzq = str(random.randint(1, 1000000000))
        idTipo = str(random.randint(1, 1000000000))
        idComa = str(random.randint(1, 1000000000))
        idParDer = str(random.randint(1, 1000000000))
        idExpresion = str(random.randint(1, 1000000000))
      
        dot.node(idFuncion, "funcion")
        dot.node(idTrunc, "trunc")
        dot.node(idParIzq, "(")
        dot.node(idTipo, self.TipoConversion)
        dot.node(idComa, ",")
        dot.node(idExpresion, "expresion")
        dot.node(idParDer, ")")

        dot.edge(idFuncion, idTrunc)
        dot.edge(idFuncion, idParIzq)
        dot.edge(idFuncion, idTipo)
        dot.edge(idFuncion, idComa)
        dot.edge(idFuncion, idExpresion)
        dot.edge(idFuncion, idParDer)

        dot, IDDotExp = self.Expresion.getAST(dot)
        dot.edge(idExpresion, IDDotExp)

        return dot, idFuncion