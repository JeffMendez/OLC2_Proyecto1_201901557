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

        else:
            
            accesoObj = entorno.getSimbolo(self.Array) # Array seria el ID que viene (id[..][..] <- id)
  
            if accesoObj.Tipo == "array":
                # Verificar indices
                indicesAcceso = []
                for indice in self.Indices:
                    exp = indice.execute(entorno)
                    if exp.Valor == "ERROR" or exp.Tipo != "Int64" or exp.Valor == 0:
                        Errores.tablaErrores.append(Error(f"El indice no es Int64, es 0 o antecede un error", self.Fila, self.Columna))
                        return Retorno("ERROR", "indice")
                    else:
                        indicesAcceso.append(exp.Valor)

                valorIndice = None
                while len(indicesAcceso) > 0: # Iterar hasta completar los indices
                    indiceActual = indicesAcceso[0]
                    try:
                        objIndice = accesoObj.Valor[indiceActual-1]
  
                        if objIndice.Tipo == "ID" or objIndice.Tipo == "array": 
                            # Pasar ref structs y arreglos, tambien funciona para array declarado adentro
                            valorIndice = objIndice.execute(entorno)
                        else:
                            # Pasar valor
                            valorIndice = objIndice
                        
                        del indicesAcceso[0] # Borra el indice ya procesado
                        accesoObj = valorIndice # Nuevo valor a iterar
                    except:
                        Errores.tablaErrores.append(Error(f"Error al acceder al indice", self.Fila, self.Columna))
                        return Retorno("ERROR", "indice")

                return Retorno(valorIndice.Valor, valorIndice.Tipo)

            else:
                Errores.tablaErrores.append(Error(f"El id no es arreglo", self.Fila, self.Columna))
                return Retorno("ERROR", "indice")

