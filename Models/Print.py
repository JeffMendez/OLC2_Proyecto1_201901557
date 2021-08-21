from Abstractos.Expresion import *

class Print(Expresion):

    def __init__(self, expresion, tipo):
        self.Expresiones = expresion
        self.Tipo = tipo
    
    def execute(self, entorno):

        salida = ""

        for exp in self.Expresiones:
            valorExp = exp.execute(None) 
            salida += str(valorExp.Valor) + " "

        if self.Tipo == "nl": 
            # Nueva linea
            #print(salida, end="")
            print("")
            print(salida)  
        else:
            # Misma linea
            #print(salida)    
            print(salida, end="")
       
        