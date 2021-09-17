from ...Abstractos.Expresion import *
from ...Abstractos.Retorno import *
from ...Abstractos.Error import *
from ...Abstractos import Globales

import random
import graphviz

class Parse(Expresion):

    def __init__(self, tipoConv, expresion, fila, columna):
        self.TipoConversion = tipoConv
        self.Expresion = expresion
        self.Fila = fila
        self.Columna = columna
    
    def execute(self, entorno):
        exp = self.Expresion.execute(entorno)

        if exp.Valor != "ERROR":

            if exp.Tipo == "struct" or exp.Tipo == "array":
                Globales.tablaErrores.append(Error(f"La conversión no es posible, el valor no es correcto", self.Fila, self.Columna))
                return Retorno("ERROR", "Parse")

            try:
                if self.TipoConversion == "Int64":
                    return Retorno(int(exp.Valor), "Int64")
                elif self.TipoConversion == "Float64":
                    return Retorno(float(exp.Valor), "Float64")
                elif self.TipoConversion == "String":
                    return Retorno(str(exp.Valor), "String")
                else:
                    Globales.tablaErrores.append(Error(f"El tipo {self.TipoConversion} no es permitido en Parse, solo String y Numericos", self.Fila, self.Columna))
                    return Retorno("ERROR", "Parse")
            except:
                Globales.tablaErrores.append(Error(f"La conversión no es posible, el valor no es correcto", self.Fila, self.Columna))
                return Retorno("ERROR", "Parse")
        else:
            return Retorno("ERROR", "Parse")

    def getAST(self, dot):
        idFuncion = str(random.randint(1, 1000000000))
        idParse = str(random.randint(1, 1000000000))
        idParIzq = str(random.randint(1, 1000000000))
        idTipo = str(random.randint(1, 1000000000))
        idComa = str(random.randint(1, 1000000000))
        idParDer = str(random.randint(1, 1000000000))
        idExpresion = str(random.randint(1, 1000000000))
      
        dot.node(idFuncion, "funcion")
        dot.node(idParse, "parse")
        dot.node(idParIzq, "(")
        dot.node(idTipo, self.TipoConversion)
        dot.node(idComa, ",")
        dot.node(idExpresion, "expresion")
        dot.node(idParDer, ")")

        dot.edge(idFuncion, idParse)
        dot.edge(idFuncion, idParIzq)
        dot.edge(idFuncion, idTipo)
        dot.edge(idFuncion, idComa)
        dot.edge(idFuncion, idExpresion)
        dot.edge(idFuncion, idParDer)

        dot, IDDotExp = self.Expresion.getAST(dot)
        dot.edge(idExpresion, IDDotExp)

        return dot, idFuncion
