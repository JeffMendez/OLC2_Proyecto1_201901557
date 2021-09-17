from flask import Flask, request, render_template
import json

from .analizador.gramatica import parse
from .analizador.Models.Entorno import *

from .analizador.Abstractos import Globales
from .analizador.Abstractos.Grafo import *

import graphviz

app = Flask(__name__)

@app.route("/execute", methods=['POST'])
def home():
    try:
        Globales.inicializar()

        entrada = request.json['input']
        Globales.entradaTxt = entrada

        if entrada != "":
            entornoGlobal = Entorno(None, "global")
            ast = parse(entrada)

            dotAST = Grafo().getGlobalDot(ast)
            dotAST.format = "png"
            dotAST.render('./app/static/ASTDOT.gv')
    
            for instruccion in ast:
                valor = instruccion.execute(entornoGlobal)

            res = {"salida": Globales.salidaPrints}

            return { 'msg': json.dumps(res), 'code': 200 }

    except Exception as e:
        print("Error al ejecutar")
        print(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return { 'msg': 'ERROR', 'code': 500 }


@app.route("/getDataRes", methods=['GET'])
def getDataRes():
    try:

        jsonErrores = None
        if len(Globales.tablaErrores) > 0:
            jsonErrores = json.dumps([ob.__dict__ for ob in Globales.tablaErrores])
        else:
            jsonErrores = json.dumps([])

        listSimbolos = []
        for ids in Globales.tablaSimbolos:
            objSimbolo = Globales.tablaSimbolos[ids]
            listSimbolos.append({'ID':ids,'Tipo':objSimbolo.Tipo,'Fila':objSimbolo.Fila,'Columna':objSimbolo.Columna})
            
        res = {"tablaErrores": jsonErrores, "tablaSimbolos": listSimbolos}

        return { 'msg': json.dumps(res), 'code': 200 }
    except:
        return { 'msg': 'ERROR', 'code': 500 }


@app.route("/getTree", methods=['GET'])
def getTree():
    try:
        return { 'msg': 'tree', 'code': 200 }
    except:
        return { 'msg': 'ERROR', 'code': 500 }

@app.route("/", methods=['GET'])
def home_view():
    return render_template('index.html')

@app.route("/analisis", methods=['GET'])
def analisis_view():
    return render_template('analisis.html')

@app.route("/reportes", methods=['GET'])
def reporte_view():
    return render_template('reportes.html')