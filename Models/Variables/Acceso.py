from Abstractos.Expresion import *
from Abstractos.Retorno import *
from Abstractos.Error import *

import Abstractos.Globales as Errores

class Acceso(Expresion):

    def __init__(self, accesoUno, accesoDos, tipo, fila, columna):
        self.AccesoUno = accesoUno
        self.AccesoDos = accesoDos
        self.Tipo = tipo
        self.Fila = fila
        self.Columna = columna 

    def execute(self, entorno):

        if self.Tipo == "ID":
            # Acceso singular - id
            simbolo = entorno.getSimbolo(self.AccesoUno)
            if simbolo == None:
                Errores.tablaErrores.append(Error(f"No existe la variable: {self.AccesoUno}", self.Fila, self.Columna))
                return Retorno("ERROR", "Variable")
            return Retorno(simbolo.Valor, simbolo.Tipo)

        elif self.Tipo == "array":
            # Acceso singular - arreglo
            return self.AccesoUno.execute(entorno)
        
        else:
            return Acceso.accMultiple(self.AccesoUno, self.AccesoDos, entorno)

    def accMultiple(accesoUno, accesoDos, entorno):

        # Recursividad accesos
        if type(accesoUno) != str:
            if accesoUno.Tipo == "mix":
                accesoUno = Acceso.accMultiple(accesoUno.AccesoUno, accesoUno.AccesoDos, entorno)

        # IDs 
        if type(accesoUno) == str:
            simbolo = entorno.getSimbolo(accesoUno)

            if simbolo.Tipo != "struct" and simbolo.Tipo != "array":
                Errores.tablaErrores.append(Error(f"No es posible el acceso, no es struct ni array: {accesoUno}", "", ""))
                return Retorno("ERROR", "Variable")
            else:
                if accesoDos == None:
                    return Retorno(simbolo.Valor, simbolo.Tipo)
                else:
                    # Caso: struct.atributo
                    if simbolo.Tipo == "struct" and type(accesoDos) == str: 
                        objStruct = simbolo.Valor

                        for attr in objStruct.Atributos:
                            if attr.ID == accesoDos:
                                if attr.Tipo == "ID":
                                    objRef = attr.Valor.execute(entorno)
                                    return Retorno(objRef.Valor, objRef.Tipo)
                                else:
                                    return Retorno(attr.Valor, attr.Tipo)
            
                        Errores.tablaErrores.append(Error(f"Atributo no existe", self.Fila, self.Columna))
                        return Retorno("ERROR", "Atributo")
        
        # Array
        elif accesoUno.Tipo == "array":
            print("acceso multiple array")

        # Struct
        elif accesoUno.Tipo == "struct":
            print(accesoUno.Valor)
            print("acc multiple strct")
