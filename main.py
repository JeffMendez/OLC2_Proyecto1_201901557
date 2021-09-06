from gramatica import parse
from Models.Entorno import *

import Abstractos.Globales as Errores

Errores.inicializar()

ast = parse()
entornoGlobal = Entorno(None, "global")

try:
    for instruccion in ast:
        valor = instruccion.execute(entornoGlobal)
        if valor != None:
            print(valor)
            if valor.Tipo == "return" or valor.Tipo == "continue" or valor.Tipo == "break":
                print("aaaaaaaaaaaaaaaaaaa")

    # Imprimir errores
    for error in Errores.tablaErrores:
        print(error.Mensaje, f"({error.Fila}:{error.Columna})")

except Exception as e:
    print("Error al ejecutar")
    print(e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
