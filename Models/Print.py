from Abstractos.Expresion import *

class Print(Expresion):

    def __init__(self, expresion, tipo):
        self.Expresiones = expresion
        self.Tipo = tipo
    
    def execute(self, entorno):

        salida = ""
        error = False

        for exp in self.Expresiones:
            valorExp = exp.execute(None)

            if valorExp.Valor == "ERROR":
                error = True
                break
            else: 
                salida += str(valorExp.Valor) + " "

        if not error:
            if self.Tipo == "nl": 
                # Nueva linea
                print("")
                print(salida)  
            else:
                # Misma linea
                print(salida, end="")
       
        