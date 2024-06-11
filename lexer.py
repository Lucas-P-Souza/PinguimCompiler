#descrção: Implementação de um lexer para a linguagem Pinguim
#import da biblioteca ply para tokenização
import ply.lex as lex

#lista de tokens
tokens = [
    'ID', 'NUMBER', 'REAL', 'STRING',
    'ASSIGN', 'COLON',
    'PLUS', 'PLUSPLUS', 'MINUS', 'MINUSMINUS', 'TIMES', 'DIVIDE', 'MODULO',
    'AND', 'OR', 'NOT',
    'EQUAL', 'GE', 'LE', 'GT', 'LT', 'NE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'DOT', 'COMMA', 'SEMICOLON',
    'INIT', 'END', 'PIN', 'POUT', 'PIF', 'PAF', 'PHILE', 'POR', 'PEGIN', 'PEND'
]

#expressões regulares para tokens simples
t_ASSIGN = r'='
t_COLON = r':'
t_PLUS = r'\+'
t_PLUSPLUS = r'\+\+'
t_MINUS = r'-'
t_MINUSMINUS = r'--'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_AND = r'and|&'
t_OR = r'or|\|'
t_NOT = r'not|~'
t_EQUAL = r'=='
t_GE = r'>='
t_LE = r'<='
t_GT = r'>'
t_LT = r'<'
t_NE = r'!='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOT = r'\.'
t_COMMA = r','
t_SEMICOLON = r';'

#palavras reservadas
reserved = {
    'init': 'INIT',
    'pinguim': 'END',
    'pin': 'PIN',
    'pout': 'POUT',
    'pif': 'PIF',
    'paf': 'PAF',
    'phile': 'PHILE',
    'pegin': 'PEGIN',
    'pend': 'PEND'
}

#tokens com regras mais complexas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_REAL(t):
    r'[-]?[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'[-]?[0-9]+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = str(t.value)
    return t

#ignorar espaços e tabulações (não são tokens)
t_ignore = ' \t'

#definir comportamento para novas linhas (incrementar o número da linha)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#tratar erros de caracteres ilegais
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

#construir o lexer
lexer = lex.lex()

#função para ler arquivo e tokenizar, imprimindo tokens no terminal
def tokenize_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)