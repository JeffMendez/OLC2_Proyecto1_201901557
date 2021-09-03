from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Abstractos.Error import *

import Abstractos.Globales as Errores

class Arreglo(Expresion):

    def __init__(self, array, tipo, indices, fila, columna):
        self.Array = array
        self.Tipo = tipo       # Si es declaracion o acceso
        self.Indices = indices
        self.Fila = fila
        self.Columna = columna

    def execute(self, entorno):
        if self.Tipo == "declaracion":
            arrayIndices = []
            # Verificacion array
            for exp in self.Array:
                valorExp = exp.execute(entorno)
                if valorExp.Valor == "ERROR":
                    return Retorno("ERROR", "array")
              
                if valorExp.Tipo == "struct":
                    # Structs y arreglos por ref se queda solo el objeto para acceso
                    arrayIndices.append(exp)
                elif valorExp.Tipo == "array":
                    # Para arreglos, verificar si es una ref o se declara dentro
                    if hasattr(exp, 'Array'):
                        # Declaracion
                        arrayIndices.append(valorExp)
                    else:
                        # Referencia
                        arrayIndices.append(exp)         
                else:
                    # Variables normales se guarda valor   
                    arrayIndices.append(valorExp)

            return Retorno(arrayIndices, "array")


