#import das funções de tokenização e parsing
from lexer import tokenize_file
from myparser import parse_file

#tupla de arquivos a serem testados
files = ('codigos_fonte/in_out.txt', 'codigos_fonte/condition.txt', 'codigos_fonte/repetition.txt', 'codigos_fonte/all.txt')

#para cada arquivo, tokeniza e faz o parsing
for filename in files:
    
    #imprime o nome do arquivo e os tokens
    print("Tokens:")
    tokenize_file(filename)

    #imprime o nome do arquivo e faz o parsing
    print("\nParsing:")
    parse_file(filename)
    print("\n")