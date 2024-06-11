import os

def translate_to_python(command_descriptions, filename):
    global translated_code
    translated_code = ""  # Limpa o conteúdo da variável de tradução

    indent_level = 0  # Nível de indentação inicial

    # Tradução das descrições dos comandos para Python
    for command in command_descriptions:
        if "INICIO DO PROGRAMA" in command:
            continue  # Ignora a descrição do início do programa
        elif "FIM DO PROGRAMA" in command:
            continue  # Ignora a descrição do fim do programa
        elif "COMANDO DE LOOP" in command:
            condition = command.split("=>")[1].strip()
            if "CONDICAO" in condition:
                condition = condition.replace("CONDICAO", "").strip()
            translated_code += "    " * indent_level + f"while {condition}:\n"

            #indent_level += 1
        elif "DESVIO CONDICIONAL" in command:
            #indent_level -= 1
            translated_code += "    " * indent_level + "else:\n"
            #indent_level += 1
        elif "CONDICIONAL" in command:
            condition = command.split("=>")[1].strip()
            if "CONDICAO" in condition:
                condition = condition.replace("CONDICAO", "").strip()
            if "pif" in condition:
                condition = condition.replace("pif", "").strip()
            translated_code += "    " * indent_level + f"if {condition}:\n"

            #indent_level += 1
        elif "ATRIBUICAO" in command:
            assignment = command
            assignment = assignment.replace("ATRIBUICAO => ", "").strip()
            if "EXPRESSAO" in assignment:
                assignment = assignment.replace("EXPRESSAO =>", "").strip()
            translated_code += "    " * indent_level + f"{assignment}\n"
        elif "EXPRESSAO" in command:
            expression = command.split("=>")[1].strip()
            translated_code += "    " * indent_level + f"{expression}\n"
        elif "COMPARACAO" in command:
            comparison = command.split("=>")[1].strip()
            translated_code += "    " * indent_level + f"if {comparison}:\n"
            #indent_level += 1
        elif "COMANDO DE ENTRADA" in command:
            var_name = command.split("pin")[1].strip()
            translated_code += "    " * indent_level + f"{var_name} = input()\n"
        elif "COMANDO DE SAIDA" in command:
            output_value = command.split("pout")[1].strip()
            print(output_value)
            translated_code += "    " * indent_level + f"print({output_value})\n"
        elif "INICIO DO BLOCO" in command:
            #translated_code += "    " * indent_level + ":\n"
            indent_level += 1
        elif "FIM DO BLOCO" in command:
            indent_level -= 1
        else:
            translated_code += command + "\n"     
    # Gerar arquivo .py
    file_name_without_extension = os.path.splitext(filename)[0]
    python_output_filename = file_name_without_extension + '_translated.py'
    with open(python_output_filename, 'w') as py_file:
        py_file.write(translated_code)
        print("Código Python traduzido foi salvo em:", python_output_filename)
