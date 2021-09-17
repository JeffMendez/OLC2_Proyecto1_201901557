from datetime import datetime

class Error:

    def __init__(self, mensaje, fila, columna):
        now = datetime.now()

        self.Mensaje = mensaje
        self.Fila = fila
        self.Columna = columna
        self.Fecha = now.strftime("%d/%m/%Y %H:%M:%S")
