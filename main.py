#esse arquivo é responsável por fazer a chamada das funções de tokenização e parsing com os arquivos de teste
#import das funções de tokenização e parsing
from lexer import tokenize_file
from myparser import parse_file

#tupla de arquivos a serem testados
files = ('codigos_fonte/in_out.txt', #arquivo de teste de entrada e saída
         'codigos_fonte/condition.txt', #arquivo de teste do 'pif' e do 'paf'
         'codigos_fonte/repetition.txt', #arquivo de teste do 'phile'
         'codigos_fonte/all.txt') #arquivo de teste com todos os comandos

#para cada arquivo, tokeniza e faz o parsing
for filename in files:
    
    #imprime o nome do arquivo e os tokens
    print("Tokens:")
    tokenize_file(filename)

    #imprime o nome do arquivo e faz o parsing
    print("\nParsing:")
    parse_file(filename)
    print("\n")