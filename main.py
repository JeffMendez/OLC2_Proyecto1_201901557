from gramatica import parse
from Models.Entorno import *

import Abstractos.Globales as Errores

Errores.inicializar()

ast = parse()
entornoGlobal = Entorno(None, "global")

try:
    for instruccion in ast:
        valor = instruccion.execute(entornoGlobal)

    # Imprimir errores
    for error in Errores.tablaErrores:
        print(error.Mensaje, f"({error.Fila}:{error.Columna})")

except Exception as e:
    print("Error al ejecutar")
    print(e)
