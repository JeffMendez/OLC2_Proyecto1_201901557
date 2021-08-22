from gramatica import parse
from Models.Entorno import *

ast = parse()
entornoGlobal = Entorno(None, "global")

try:
    for instruccion in ast:
        valor = instruccion.execute(entornoGlobal)

        #if valor.Valor != "ERROR":
        #    print(f"Res: {valor.Valor} , tipo: {valor.Tipo}")
            
except Exception as e:
    print("Error al ejecutar")
    print(e)
