from gramatica import parse

ast = parse()

try:
    for instruccion in ast:
        valor = instruccion.execute(None)

        if valor.Valor != "ERROR":
            print(f"Res: {valor.Valor} , tipo: {valor.Tipo}")
            
except Exception as e:
    print("Error al ejecutar")
    print(e)
