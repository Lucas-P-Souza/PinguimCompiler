#esse arquivo é reponsável por traduzir os comandos da linguagem Pinguim para Python
#import do modulo os
import os

'''
Observação: 

    Esse código trata a lista command_descriptions enviada pelo mypaser,
    dessa forma, ela vem carregada de "lixo", o que estamos removendo enquanto traduzimos.
    Exemplo de uma string com "lixo":

        CONDICIONAL => pif (CONDICAO a == b)

    Nesse caso deveremos remover a string "CONDICIONAL => " e a "CONDICAO ", assim,
    no final ficaremos com a string:

        pif (a == b)

    Com isso podemos traduzir a palavra reservada do Pinguim 'pif' para a palavra "if" do python.

    Dessa forma, quando forem citadas palavras em CAIXA ALTA e entre "aspas duplas" estará sendo 
    referenciado o reconhecimento dos tokens, dessa maneira ao dizer que "CONDICAO" será removida,
    isso siginifica que a string "CONDICAO" - lixo da lista command_descriptions - que será removida 
    da string que está sendo traduzida e não a condicao própriamente dita.
'''

#função responsável pela tradução
def translate_to_python(command_descriptions, filename, output_folder_py):
    
    #define a variável global que receberá o código traduzido e limpa ela logo em seguida para 
    # evitar restos de compilações anteriores
    global translated_code
    translated_code = ""  
    
    array_of_atribs = []

    #nível de indentação inicial, essa variável será incrementada ou decrementada conforme 
    # forem sendo reconhcidas as aberturas ou fechamente dos blocos de comandos
    indent_level = 0  

    #tradução das descrições dos comandos para Python, conforme a lista command_descriptions
    for command in command_descriptions:
        if "INICIO DO PROGRAMA" in command:
            #ignora a descrição do início do programa, uma vez que, no python não há a identificação
            # de inicio de programa
            continue  
        
        elif "FIM DO PROGRAMA" in command:
            #ignora a descrição do fim do programa, uma vez que, no python não há a identificação
            # de fim de programa
            continue  
        
        elif "COMANDO DE LOOP" in command:
            #trata o caso de phile
            #tira a string "COMANDO DE LOOP =>"
            condition = command.split("=>")[1].strip()
            
            #Caso haja uma "CONDICAO" deve-se remover string "CONDICAO"
            if "CONDICAO" in condition:
                condition = condition.replace("CONDICAO ", "").strip()
                
            #adiciona na string da tradução o comando de while, junto com a sua condição
            #o próprio tradutor coloca while pois é a unica estrutura ded repetição que estamos trabalhando
            translated_code += "    " * indent_level + f"while {condition}:\n"
        
        elif "DESVIO CONDICIONAL" in command:
            #adiciona o else quando reconhcer o desvio condicional
            #não trabalhamos com elif, então já colocamo o else no hardcode
            translated_code += "    " * indent_level + "else:\n"
        
        elif "CONDICIONAL " in command:
            #trata os casos de PIF
            #pega a string pra frente da =>
            condition = command.split("=>")[1].strip()
            
            #quando encontrar uma condição dentro do pif, deve remover a string "CONDICAO"
            if "CONDICAO" in condition:
                condition = condition.replace("CONDICAO ", "").strip()
                
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
            
            #caso a atribuição seja feita com ":" ao invés de "=" deve-se trocar
            if ":" in assignment:    
                assignment = assignment.replace(":", "=").strip()
            
            #caso a atribuição seja feita com "TERMO" ao invés de um numero na frente do "="
            if "TERMO" in assignment:
                assignment = assignment.replace("TERMO ", "").strip()
                
            #adiciona a string no lista traduzida, já sem o "lixo", ficando somente: 
            # variável = alguma coisa
            array_of_atribs.append(assignment[0:assignment.find(" =")])
            translated_code += "    " * indent_level + f"{assignment}\n"
        
        elif "EXPRESSAO" in command:
            #trata o caso das expressões
            #remove deixa apenas o que estiver a frente da => e adicona na lista traduzida
            expression = command.split("=>")[1].strip()
            if "TERMO" in expression:
                expression = expression.replace("TERMO ", "").strip()
            translated_code += "    " * indent_level + f"{expression}\n"
        
        elif "COMPARACAO" in command:
            comparison = command.split("=>")[1].strip()
            translated_code += "    " * indent_level + f"if {comparison}:\n"
        
        elif "COMANDO DE ENTRADA" in command:
            #trata o caso do pin
            #basta remover o pin e adicionar "= input()" em frente à varaivel que ficará
            var_name = command.split("pin")[1].strip()
            if var_name in array_of_atribs:
                translated_code += "    " * indent_level + f"{var_name} = int(input())\n"
            else:
                translated_code += "    " * indent_level + f"{var_name} = input()\n"
        
        elif "COMANDO DE SAIDA" in command:
            #trata o caso do pout
            #para isso deve-se remover o pout e colocar o que estava a sua frente dentro de um print()
            output_value = command.split("pout")[1].strip()
            #print(output_value)
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
    file_name_without_extension = os.path.splitext(os.path.basename(filename))[0]
    python_output_filename = os.path.join(output_folder_py, file_name_without_extension + '_translated.py')
    with open(python_output_filename, 'w') as py_file:
        py_file.write(translated_code)
        print("Código Python traduzido foi salvo em:", python_output_filename)