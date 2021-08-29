from Abstractos.Expresion import *
from Abstractos.Retorno import *

class Arreglo(Expresion):

    def __init__(self, array, tipo, indices):
        self.Array = array
        self.Tipo = tipo       # Si es declaracion o acceso
        self.Indices = indices # 

    def execute(self, entorno):
        if self.Tipo == "declaracion":

            # Verificacion array
            for exp in self.Array:
                valorExp = exp.execute(entorno)
                if valorExp.Valor == "ERROR":
                    return Retorno("ERROR", "array")
            return Retorno(self.Array, "array")

        else:
            objeto = self.Array.execute(entorno)
            if objeto.Tipo == "array":
                # Verificar indices
                indicesAcceso = []
                for indice in self.Indices:
                    exp = indice.execute(entorno)
                    if exp.Valor == "ERROR" or exp.Tipo != "Int64":
                        return Retorno("ERROR", "indice")
                    else:
                        indicesAcceso.append(exp.Valor)

                valorIndice = None
                while len(indicesAcceso) > 0: # Iterar hasta completar los indices
                    indiceActual = indicesAcceso[0]
                    try:
                        valorIndice = objeto.Valor[indiceActual].execute(entorno)
                        del indicesAcceso[0] # Borra el indice ya procesado
                        objeto = valorIndice # Nuevo valor a iterar
                    except:
                        print("Error al acceder")
                        return Retorno("ERROR", "indice")

                return Retorno(valorIndice.Valor, valorIndice.Tipo)
            else:
                print("el id no es arreglo")
                return Retorno("ERROR", "indice")

