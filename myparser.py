import ply.yacc as yacc
import translator as tr
import os
from lexer import tokens

# Lista para armazenar as descrições dos comandos
command_descriptions = []

def p_program(p):
    '''program : INIT commands END'''
    command_descriptions.append("INICIO DO PROGRAMA => " + p[1])
    command_descriptions.extend(p[2])
    command_descriptions.append("FIM DO PROGRAMA => " + p[3])
    p[0] = "Programa reconhecido"

def p_commands(p):
    '''commands : command
                | command commands'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

def p_command(p):
    '''command : assignment
               | conditional
               | loop
               | input
               | output
               | block'''
    p[0] = p[1]

def p_assignment(p):
    '''assignment : ID ASSIGN expression
                  | ID ASSIGN STRING'''
    p[0] = ["ATRIBUICAO => " + p[1] + " = " + str(p[3])]

def p_expression(p):
    '''expression : term
                  | term PLUS expression
                  | term MINUS expression
                  | LT ID GT'''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '<' and p[3] == '>':
        p[0] = f"COMPARACAO {p[2]} {p[3]}"
    else:
        p[0] = f"EXPRESSAO => {p[1]} {p[2]} {p[3]}"

def p_term(p):
    '''term : factor
            | factor TIMES term
            | factor DIVIDE term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"TERMO {p[1]} {p[2]} {p[3]}"

def p_factor(p):
    '''factor : NUMBER
              | REAL
              | ID
              | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_conditional(p):
    '''conditional : PIF LPAREN condition RPAREN block optional_else
                   | PIF LPAREN condition RPAREN block'''
    p[0] = ["CONDICIONAL => " + p[1] + " (" + p[3] + ")"] + p[5]
    if len(p) == 7:
        p[0] += p[6]

def p_optional_else(p):
    '''optional_else : PAF block
                     | empty'''
    if len(p) == 3:
        p[0] = ["DESVIO CONDICIONAL => " + p[1]] + p[2]
    else:
        p[0] = []

def p_condition(p):
    '''condition : expression relational_op expression'''
    p[0] = f"CONDICAO {p[1]} {p[2]} {p[3]}"

def p_relational_op(p):
    '''relational_op : EQUAL
                     | GE
                     | LE
                     | GT
                     | LT
                     | NE'''
    p[0] = p[1]

def p_loop(p):
    '''loop : PHILE LPAREN condition RPAREN block'''
    p[0] = ["COMANDO DE LOOP => (" + p[3] + ")"] + p[5]

def p_increment(p):
    '''increment : ID PLUSPLUS
                 | ID MINUSMINUS'''
    p[0] = []

def p_block(p):
    '''block : LBRACE commands RBRACE
             | LBRACE commands PEND
             | PEGIN commands RBRACE
             | PEGIN commands PEND'''
    p[0] = ["INICIO DO BLOCO => " + p[1]] + p[2] + ["FIM DO BLOCO => " + p[3]]

def p_input(p):
    '''input : PIN ID'''
    p[0] = ["COMANDO DE ENTRADA => " + p[1] + " " + p[2]]

def p_output(p):
    '''output : POUT expression
              | POUT STRING'''
    p[0] = ["COMANDO DE SAIDA => " + p[1] + " " + str(p[2])]

def p_empty(p):
    '''empty :'''
    p[0] = []

def p_error(p):
    if p:
        print(f"Erro de sintaxe no token '{p.value}', linha {p.lineno}")
    else:
        print("Erro de sintaxe no final do arquivo")

parser = yacc.yacc()

def parse_file(filename):
    global command_descriptions

    # Extrair o nome do arquivo sem a extensão
    file_name_without_extension = os.path.splitext(filename)[0]
    output_filename = file_name_without_extension + '_commands_output.txt'

    with open(filename, 'r') as file:
        data = file.read()
    
    # Reinicializar command_descriptions
    command_descriptions = []
    
    parser.parse(data)
    
    # Escrever as descrições dos comandos no arquivo de saída (modo de escrita)
    with open(output_filename, 'w') as out_file:
        for description in command_descriptions:
            if isinstance(description, list):  # Verifica se é uma lista de comandos
                for cmd in description:
                    out_file.write(cmd + "\n")
                    print(cmd)
            else:
                out_file.write(description + "\n")
                print(description)

    # Traduzir para Python
    print("\nSaída do arquivo", filename, " traduzido para Python:")
    tr.translate_to_python(command_descriptions, filename)
