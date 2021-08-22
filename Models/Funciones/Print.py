from Abstractos.Expresion import *

class Print(Expresion):

    # PENDIENTE ARREGLO DE SALIDAS NUEVA LINEA
    
    def __init__(self, expresion, tipo):
        self.Expresiones = expresion
        self.Tipo = tipo
    
    def execute(self, entorno):

        salida = ""
        error = False

        for exp in self.Expresiones:
            valorExp = exp.execute(entorno)

            if valorExp.Valor == "ERROR":
                error = True
                break
            else:
                if valorExp.Tipo == "Nulo": valorExp.Valor = "nothing" # Impresion unica para nothing
                salida += str(valorExp.Valor) + " "

        if not error:
            if self.Tipo == "nl": 
                # Nueva linea
                print(salida)  
            else:
                # Misma linea
                print(salida, end="")
       
        