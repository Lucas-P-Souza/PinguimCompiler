#descrição: Módulo de tradução para python
#import do modulo os
import os

'''observação: esse código trata a lista command_descriptions enviada pelo mypaser,
    dessa forma, ela vem carregada de "lixo", o que estamos removendo enquanto traduzimos
    exemplo de uma string com "lixo":
    
        CONDICIONAL => pif (CONDICAO a == b)
    
    nesse caso deveremos remover a string "CONDICIONAL => pif" e a "CONDICAO", assim,
    no final ficaremos com a string:

        ( a == b)
        
    com isso podemos adicionar a palavra reservada do python "if"
'''

#função responsável pela tradução
def translate_to_python(command_descriptions, filename):
    global translated_code
    #limpa o conteúdo da variável de tradução (prepara para um nova tradução)
    translated_code = ""  

    #nível de indentação inicial
    indent_level = 0  

    #tradução das descrições dos comandos para Python
    for command in command_descriptions:
        if "INICIO DO PROGRAMA" in command:
            #ignora a descrição do início do programa
            continue  
        elif "FIM DO PROGRAMA" in command:
            #ignora a descrição do fim do programa
            continue  
        elif "COMANDO DE LOOP" in command:
            #trata o caso de phile
            #tira a string "COMANDO DE LOOP =>"
            condition = command.split("=>")[1].strip()
            #Caso haja uma "CONDICAO" deve-se remover string "CONDICAO"
            if "CONDICAO" in condition:
                condition = condition.replace("CONDICAO", "").strip()
            #adiciona na string da tradução o comando de while, junto com a sua condição
            #o próprio tradutor coloca while pois é a unica estrutura ded repetição que estamos trabalhando
            translated_code += "    " * indent_level + f"while {condition}:\n"
        elif "DESVIO CONDICIONAL" in command:
            #adiciona o else quando reconhcer o desvio condicional
            #não trabalhamos com elif, então já colocamo o else no hardcode
            translated_code += "    " * indent_level + "else:\n"
        elif "CONDICIONAL" in command:
            #trata os casos de PIF
            #pega a string pra frente da =>
            condition = command.split("=>")[1].strip()
            #quando encontrar uma condição dentro do pif, deve remover o "CONDICAO"
            if "CONDICAO" in condition:
                condition = condition.replace("CONDICAO", "").strip()
            #quando encontrar um  pif na string tb deve ser removido
            if "pif" in condition:
                condition = condition.replace("pif", "").strip()
            #adiciona o if no começo, seguido da condição sem "lixo"
            translated_code += "    " * indent_level + f"if {condition}:\n"
        elif "ATRIBUICAO" in command:
            #trata o caso das atribuições de valores às variáveis
            assignment = command
            #remove o começo da string que é: "ATRIBUICAO =>"
            assignment = assignment.replace("ATRIBUICAO => ", "").strip()
            #caso o que estiver sendo atribuido à variável seja uma expressão e nao um valor
            if "EXPRESSAO" in assignment:
                #remove o "lixo" da string
                assignment = assignment.replace("EXPRESSAO =>", "").strip()
            #adiciona a string no lista traduzida, já sem o "lixo", ficando somente: 
            # variável = alguma coisa
            translated_code += "    " * indent_level + f"{assignment}\n"
        elif "EXPRESSAO" in command:
            #trata o caso das expressões
            #remove deixa apenas o que estiver a frente da => e adicona na lista traduzida
            expression = command.split("=>")[1].strip()
            translated_code += "    " * indent_level + f"{expression}\n"
        elif "COMPARACAO" in command:
            comparison = command.split("=>")[1].strip()
            translated_code += "    " * indent_level + f"if {comparison}:\n"
        elif "COMANDO DE ENTRADA" in command:
            #trata o caso do pin
            #basta remover o pin e adicionar "= input()" em frente à varaivel que ficará
            var_name = command.split("pin")[1].strip()
            translated_code += "    " * indent_level + f"{var_name} = input()\n"
        elif "COMANDO DE SAIDA" in command:
            #trata o caso do pout
            #para isso deve-se remover o pout e colocar o que estava a sua frente dentro de um print()
            output_value = command.split("pout")[1].strip()
            print(output_value)
            translated_code += "    " * indent_level + f"print({output_value})\n"
        elif "INICIO DO BLOCO" in command:
            #adiciona as indentações conforme os bloco de comando forem sendo abertos ("{" ou "peguin")
            indent_level += 1
        elif "FIM DO BLOCO" in command:
            #remove as indentações conforme os bloco de comando forem sendo fechados ("}" ou "pend")
            indent_level -= 1
        else:
            translated_code += command + "\n"     
    
    #módulo responsável por criar o arquivo .py que podera ser compilado pelo próprio compilador
    #   da linguagem python
    file_name_without_extension = os.path.splitext(filename)[0]
    #utiliza o sufixo _translated.py para identificar os arquivos aqui gerados
    python_output_filename = file_name_without_extension + '_translated.py'
    with open(python_output_filename, 'w') as py_file:
        py_file.write(translated_code)
        print("Código Python traduzido foi salvo em:", python_output_filename)
