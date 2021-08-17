from gramatica import parse

ast = parse()

try:
    for instruccion in ast:
        valor = instruccion.execute(None)
        print(valor.Valor)
except Exception as e:
    print("Error al ejecutar")
    print(e)
