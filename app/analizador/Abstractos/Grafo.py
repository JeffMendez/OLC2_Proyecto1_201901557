import random
import graphviz

class Grafo:

    def __init__(self):
        self.Dot = graphviz.Digraph(comment='AST JOLC')

    def getGlobalDot(self, instrucciones):
        idPadre = str(random.randint(1, 1000000000))
        idInstrucciones = str(random.randint(1, 1000000000))

        self.Dot.node(idPadre, "AST")
        self.Dot.node(idInstrucciones, "instrucciones")
        self.Dot.edge(idPadre, idInstrucciones)

        for instr in instrucciones:
            idInstr = str(random.randint(1, 1000000000))
            self.Dot.node(idInstr, "instruccion")
            self.Dot.edge(idInstrucciones, idInstr)

            self.Dot, idDotInst = instr.getAST(self.Dot) # Que se agrege el dot y enviar el id para el edge
            self.Dot.edge(idInstr, idDotInst)

        return self.Dot



    
