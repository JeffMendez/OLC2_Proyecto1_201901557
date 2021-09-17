
from ..Abstractos.Expresion import *
from ..Abstractos.Retorno import *
from ..Models.Entorno import *

class Bloque(Expresion):

    def __init__(self, instrucciones):
        self.Instrucciones = instrucciones
   
    def execute(self, entorno):
        nuevoEntorno = Entorno(entorno, "")
        for inst in self.Instrucciones:
            retornoInst = inst.execute(nuevoEntorno)

            if retornoInst != None:
                if retornoInst.Tipo == "continue" or retornoInst.Tipo == "break" or retornoInst.Tipo == "return":
                    return retornoInst
                    # if inst.Tipo == "return":
                    #     print("entra 1")
                    #     return retornoInst


    def getAST(self, dot):
        idInstrucciones = str(random.randint(1, 1000000000))

        dot.node(idInstrucciones, "instrucciones")

        for instr in self.Instrucciones:
            idInstr = str(random.randint(1, 1000000000))
            dot.node(idInstr, "instruccion")
            dot.edge(idInstrucciones, idInstr)

            dot, idDotInst = instr.getAST(dot) # Que se agrege el dot y enviar el id para el edge
            dot.edge(idInstr, idDotInst)

        return dot, idInstrucciones
