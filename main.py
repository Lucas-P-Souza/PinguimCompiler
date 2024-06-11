from lexer import tokenize_file
from myparser import parse_file

# Nome do arquivo a ser lido
files = ('codigos_fonte/in_out.txt', 'codigos_fonte/condition.txt', 'codigos_fonte/repetition.txt', 'codigos_fonte/all.txt')

for filename in files:
    
    print("Tokens:")
    tokenize_file(filename)

    print("\nParsing:")
    parse_file(filename)
    print("\n")