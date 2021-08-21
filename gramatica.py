from Models.Aritmetica import *
from Models.Relacional import *
from Models.Logico import *

from Models.Simbolo import *

from Models.Print import *

rw = {
    "true": "TRUE",
    "false": "FALSE",
    "nothing": "NOTHING",

    "Evaluar": "REVALUAR",

    "println": "PRINTLN",
    "print": "PRINT",
}

tokens  = [
    "ID",

    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',

    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'POTENCIA',
    'MODULO',

    'MAYOR',
    'MENOR',
    'MAYIGUAL',
    'MENIGUAL',
    'IGUALDAD',
    'DISTINTO',

    'OR',
    'AND',
    'NOT',

    'DECIMAL',
    'ENTERO',
    'STRING',
    'CHAR',

    'PTCOMA',
    'COMA',

] + list(rw.values())

# Tokens
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_CORIZQ    = r'\['
t_CORDER    = r'\]'

t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_POTENCIA  = r'\^'
t_MODULO    = r'%'

t_MAYOR     = r'>'
t_MENOR     = r'<'
t_MAYIGUAL  = r'>='
t_MENIGUAL  = r'<='
t_IGUALDAD  = r'=='
t_DISTINTO  = r'!='

t_OR        = r'\|\|'
t_AND       = r'&&'
t_NOT       = r'!'

t_PTCOMA    = r';'
t_COMA      = r','

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    #t.type = rw.get(t.value.upper(), 'ID')
    t.type = rw.get(t.value,'ID')
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Error al parsear float %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Error al parsear int %d", t.value)
        t.value = 0
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_CHAR(t):
    r'\'.?\''
    t.value = t.value[1:-1]
    return t

# Caracteres ignorados
t_ignore = " \t"

def t_MLCOMMENT(t):
    r'\#=(.|\n)*?=\#'
    t.lexer.lineno += t.value.count("\n")

def t_OLCOMMENT(t):
    r'\#.*\n'
    t.lexer.lineno += 1
    
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('left','IGUALDAD','DISTINTO'),
    ('left','MAYOR','MENOR','MAYIGUAL','MENIGUAL'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('left','POTENCIA'),
    ('left','MODULO'),
    ('right','NOT'),
    ('right','UMENOS'),
)

# Definición de la gramática
def p_inicio(t):
    'start : instrucciones'
    t[0] = t[1]
    return t[0]

def p_instrucciones(t):
    '''instrucciones    : instrucciones instruccion 
                        | instruccion '''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]

def p_instruccion(t):
    'instruccion  : printInst PTCOMA'
    t[0] = t[1]

def p_instruccion_print(t):
    'printInst : PRINT PARIZQ paramExp PARDER'
    t[0] = Print(t[3], "l")

def p_instruccion_println(t):
    'printInst : PRINTLN PARIZQ paramExp PARDER'
    t[0] = Print(t[3], "nl")

def p_param_expresion(t):
    '''paramExp     : paramExp COMA expresion
                    | expresion'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[3])
        t[0] = t[1]

def p_expresion_binaria(t):
    '''expresion    : expresion MAS expresion
                    | expresion MENOS expresion
                    | expresion POR expresion
                    | expresion DIVIDIDO expresion
                    | expresion POTENCIA expresion
                    | expresion MODULO expresion
                    
                    | expresion MAYOR expresion
                    | expresion MENOR expresion
                    | expresion MAYIGUAL expresion
                    | expresion MENIGUAL expresion
                    | expresion IGUALDAD expresion
                    | expresion DISTINTO expresion
                    
                    | expresion AND expresion
                    | expresion OR expresion'''
        
    if t[2] == '+': 
        t[0] = Aritmetica(t[1], t[3], "+", t.lineno(2), t.lexpos(2))
    elif t[2] == '-':
        t[0] = Aritmetica(t[1], t[3], "-", t.lineno(2), t.lexpos(2))
    elif t[2] == '*': 
        t[0] = Aritmetica(t[1], t[3], "*", t.lineno(2), t.lexpos(2))
    elif t[2] == '/': 
        t[0] = Aritmetica(t[1], t[3], "/", t.lineno(2), t.lexpos(2))
    elif t[2] == '^': 
        t[0] = Aritmetica(t[1], t[3], "^", t.lineno(2), t.lexpos(2))
    elif t[2] == '%': 
        t[0] = Aritmetica(t[1], t[3], "%", t.lineno(2), t.lexpos(2))
    
    elif t[2] == '>': 
        t[0] = Relacional(t[1], t[3], ">", t.lineno(2), t.lexpos(2))
    elif t[2] == '<': 
        t[0] = Relacional(t[1], t[3], "<", t.lineno(2), t.lexpos(2))
    elif t[2] == '>=': 
        t[0] = Relacional(t[1], t[3], ">=", t.lineno(2), t.lexpos(2))
    elif t[2] == '<=': 
        t[0] = Relacional(t[1], t[3], "<=", t.lineno(2), t.lexpos(2))
    elif t[2] == '==': 
        t[0] = Relacional(t[1], t[3], "==", t.lineno(2), t.lexpos(2))
    elif t[2] == '!=': 
        t[0] = Relacional(t[1], t[3], "!=", t.lineno(2), t.lexpos(2))
    
    elif t[2] == '&&': 
        t[0] = Logico(t[1], t[3], "and", t.lineno(2), t.lexpos(2))
    elif t[2] == '||': 
        t[0] = Logico(t[1], t[3], "or", t.lineno(2), t.lexpos(2))

def p_expresion_unaria(t):
    '''expresion    : MENOS expresion %prec UMENOS
                    | NOT expresion %prec UMENOS'''

    if t[1] == "-":
        t[0] = Aritmetica(t[2], None, "umenos", t.lineno(1), t.lexpos(1))
    else:
        t[0] = Logico(t[2], None, "not", t.lineno(1), t.lexpos(1))

def p_expresion_agrupacion(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

def p_expresion_basica(t):
    '''expresion    : ENTERO
                    | DECIMAL
                    | STRING
                    | CHAR
                    | TRUE
                    | FALSE
                    | NOTHING
                    | ID'''  
    tipo = t.slice[1].type

    if tipo == "ENTERO":
        t[0] = Simbolo(t[1], "Int64", None)
    elif tipo == "DECIMAL":
        t[0] = Simbolo(t[1], "Float64", None)
    elif tipo == "STRING":
        t[0] = Simbolo(t[1], "String", None)
    elif tipo == "CHAR":
        t[0] = Simbolo(t[1], "Char", None)
    elif isinstance(t[1], str):
        value = str(t[1])
        if "true" in value:
            t[0] = Simbolo(True, "Bool", None)
        elif "false" in value:
            t[0] = Simbolo(False, "Bool", None)
        elif "nothing" in value:
            t[0] = Simbolo(None, "Nulo", None) 
            
def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

def parse():
    f = open("./entrada.txt", "r")
    input = f.read()
    #print(input)
    return parser.parse(input)