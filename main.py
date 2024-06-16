#esse arquivo é responsável por fazer a chamada das funções de tokenização e parsing com os arquivos de teste
#import das funções de tokenização e parsing
from lexer import tokenize_file
from myparser import parse_file
from builder import generate_executables
import os

#caminho da pasta onde estão os arquivos .pin
folder_path = 'src_files/'

#caminhos das pastas de saída dos arquivos .txt, .py, .spec e dos .exe
output_folder_txt = 'output_txt/'
output_folder_py = 'output_py/'
output_folder_spec = 'output_spec/' #sera removida após a geração dos executáveis
dist_folder_name = 'output_exe/'

#caso as pastas de saída não existam, elas são criadas
os.makedirs(output_folder_txt, exist_ok=True)
os.makedirs(output_folder_py, exist_ok=True)
os.makedirs(output_folder_spec, exist_ok=True)
os.makedirs(dist_folder_name, exist_ok=True)

#verifica se o arquivo é um arquivo .pin
def is_pin_file(filename):
    return filename.endswith('.pin')

#listar todos os arquivos na pasta para compilação
all_files = os.listdir(folder_path)

#para cada arquivo, tokeniza e faz o parsing
for filename in all_files:
    
    file_path = os.path.join(folder_path, filename)
    
    if is_pin_file(filename):
        
        #diz qual arquivo está sendo compilado, que é o arquivo que está sendo tokenizado e parseado
        print(f"Compilando arquivo: {file_path}\n")

        #imprime os tokens do arquivo
        #que são os elementos da linguagem que foram identificados
        print("Tokens:")
        tokenize_file(file_path)

        #imprime o parsing do arquivo
        #que é a tradução dos tokens para comandos da linguagem
        print("\nParsing:")
        parse_file(file_path, output_folder_txt, output_folder_py)
        print("\n")
        
    else:
        #caso o arquivo não seja .pin, ele não será processado
        print(f"Erro: O arquivo '{filename}' não possui a extensão .pin e não será processado.\n")

generate_executables(output_folder_py, output_folder_spec, dist_folder_name)