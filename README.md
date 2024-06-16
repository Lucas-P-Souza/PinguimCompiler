# Resumo do README
    
        Este arquivo README tem o intuito de explicar o funcionamento e a estrutura de um analisador 
        de código fonte desenvolvido para a disciplina ECOM06A – Compiladores, ministrada pela 
        Professora Thatyana de Faria Piola Seraphim. O projeto foi elaborado pelo grupo composto por 
        Lucas de Paula Souza, Luiz Fernando Costa Silva, Ryan Alves Mazzeu e Vinícius Gomes de Araújo.
    
        O objetivo principal deste projeto é implementar um analisador léxico e sintático além de um 
        "tradutor"para a linguagem de programação Pinguim, criada pelo grupo. A linguagem Pinguim, 
        inspirada na linguagem C,possui sintaxe e estruturas de controle semelhantes, o que facilita 
        o entendimento dos comandos para programadores familiarizados com C.
    
        O projeto utiliza a biblioteca Ply (Python Lex-Yacc) para realizar a tokenização do código 
        fonte e a análise sintática, gerando descrições dos comandos presentes no código. Este README 
        detalha a linguagem Pinguim, a estrutura dos arquivos de código, o processo de compilação e 
        execução, além de fornecer exemplosde código e seus respectivos resultados de análise.
    
        É valido lembrar que nem todas as expressões regulares apresentadas na 1ª etapa do trabalho 
        foram implementadas, algumas foram modificadas e outras não estão presentes no código.

# Matéria    
    
        ECOM06A – Compiladores 

# Professora
    
        Dra. Profa. Thatyana de Faria Piola Seraphim

# Grupo:

## Integrante | Matrícula | Email

        Lucas de Paula Souza      | 2022013072 | lucassouzavga@gmail.com 
        Luiz Fernando Costa Silva | 2022003915 | luiz.fernandocsilva17@gmail.com 
        Ryan Alves Mazzeu         | 2022002186 | ryanmazzeu111@gmail.com 
        Vinícius Gomes de Araújo  | 2022003334 | d2022003334@unifei.edu.br

# Descrição do Projeto

        Este projeto consiste em um analisador de código fonte escrito em Python, capaz de 
        tokenizar o código, gerar descrições dos comandos presentes nele com base nalinguagem 
        Pinguim e traduzi-lo para python. O projeto utiliza a biblioteca Ply (Python Lex-Yacc) 
        para implementar tanto o analisador léxico quanto o sintático. Além disso, há uma 
        funcionalidade de tradução dos comandos da linguagem Pinguim para Python, facilitando 
        a execução dos programas escritos em Pinguim ".pin".

# Linguagem Pinguim

        A linguagem de programação Pinguim foi criada pelo grupo durante um trabalho da disciplina
        Compiladores (ECOM06A) e possui a extensão ".pin". Pinguim é uma linguagem C-like, ou seja, 
        é uma linguagem de programação cuja sintaxe, estrutura e paradigmas de certa forme se 
        assemelham aos da linguagem C. Isso significa que a Pinguim possui elementos que são 
        facilmente reconhecíveis por programadores familiarizados com C.

##  Semelhanças Pinguim x C

###     Sintaxe 

            Utiliza uma sintaxe semelhante, com chaves '{}' para definir blocos de código, em 
            Pinguimtambém pode-se usar 'pegin' e 'pend' para abrir e fechar os blocos de comando 
            respectivamente.

###     Estruturas de controle 

            Possuem estruturas de controle como 'pif', 'paf' e 'phile' que respectivamente se 
            comportam de maneira semelhante à 'if', 'else' e 'while' de C.

###     Operadores 

            Utilizam operadores aritméticos ('+', '-', '*', '/', '%'), lógicos (['&', 'and'], 
            ['|', 'or'], '!'),e de comparação ('equal', 'dif', '<', '>', '<=', '>=') que 
            funcionam de maneira similar aos do C.

# Descrição do diretório do Código (contém as definições dos arquivos iniciais e dos que serão gerados pelo compilador)

##  Lexer (lexer.py)

        Este arquivo contém a definição do lexer usando a biblioteca Ply. O lexer é 
        responsável por tokenizar o código fonte, ou seja, converter o código em uma 
        sequência de tokens que representam palavras-chave, identificadores, operadores, 
        números, etc.

##  Myparser (myparser.py)

        Neste arquivo está contida a definição do parser utilizando a biblioteca Ply. 
        O parser analisa a estrutura do código fonte tokenizado e gera descrições dos
        comandos presentes no código.

##  Translator (translator.py)

        Dentro deste arquivo está a função responsável por traduzir as descrições dos 
        comandos geradas pelo parser para código Python. A função translate_to_python 
        lê as descrições, converte cada comando em uma instrução Python equivalente e 
        salva o resultado em um arquivo .py.

##  Builder (builder.py)

        Dentro deste arquivo, a função principal é gerenciar a criação dos executáveis
        a partir dos scripts Python traduzidos. Utilizamos o PyInstaller para empacotar
        os arquivos Python gerados pelo tradutor em executáveis independentes. O processo
        inclui a verificação e criação automática da pasta output_exe se não existir, 
        garantindo que os programas em Pinguim sejam facilmente distribuídos e executados 
        em diferentes ambientes sem a necessidade de instalação prévia do Python.

##  Main (main.py):

        Este arquivo é o script principal do projeto. Ele executa o processo completo de 
        tokenização e análise sintática dos exemplos de códigos presentes nos arquivos 
        de entrada. Além disso, ele imprime as descrições dos comandos resultantes no 
        terminal e também as escreve em arquivos de saída (.txt).
    
##  Parsetab (parsetab.py)

        Este é um arquivo gerado automaticamente pela biblioteca Ply. Ele contém a tabela 
        de análise sintática (parsing table) utilizada pelo Ply para processar a gramática 
        definida no myparser.py. Essencial para o funcionamento do parser, este arquivo não 
        deve ser editado.

## Parser (parser.out) 

        Este arquivo contém a saída gerada pelo processo de tradução do código fonte. Após o 
        código fonte ter sido tokenizado e analisado sintaticamente, as descrições dos comandos 
        são traduzidas para código Python pela função translate_to_python, conforme definido no 
        arquivo Translator (translator.py). Cada comando é convertido em uma instrução Python 
        equivalente e o resultado é armazenado neste arquivo .out.

        O conteúdo deste arquivo representa a versão Python dos comandos presentes no código 
        fonte original, prontos para serem executados ou manipulados conforme necessário.

##  Pycache (./__pycache__) 

        Este diretório gerado automaticamente pelo Python. Contém arquivos de cache (bytecode compilado)
        que aceleram a execução dos programas. O Python compila os scripts em bytecode (.pyc files)
        e os armazena nessa pasta para uso futuro. Esses arquivos são:

            - lexer.cpython-312.pyc: Bytecode compilado para lexer.py.
            - myparser.cpython-312.pyc: Bytecode compilado para myparser.py.
            - parsetab.cpython-312.pyc: Bytecode compilado para parsetab.py.
            - translator.cpython-312.pyc: Bytecode compilado para translator.py.

##  Source Files (./src_filles)

        Este diretório contém os exemplos de códigos fonte a serem analisados. Para
        que os arquivos sejam compilados eles devem estar na extenção da linguagem ".pin".

                - in_out.pin
                - condition.pin
                - repetition.pin
                - all.pin
            
##  Output .txt (./output_txt)

        Este diretório contém os arquivos de saída resultantes da análise sintática dos arquivos 
        de entrada.

                - in_out_commands_output.txt
                - condition_commands_output.txt
                - repetition_commands_output.txt
                - all_commands_output.txt

##  Output .py (./output_py)

        Este diretório contém os arquivos de saída resultantes da tardução dos arquivos de entrada 
        para python.

                - in_out_translated.py
                - condition_translated.py
                - repetition_translated.py
                - all_translated.py

##  Output .exe (./output_exe)

        Este diretório contém os arquivos executáveis gerados pelo builder a partir dos arquivos .py 
        resultandes da tradução

                - in_out.exe
                - condition.exe
                - repetition.exe
                - all.exe


# Arquivos de Entrada (./src_filles/ -> in_out.pin, condition.pin, repetition.pin, all.pin)

##  in_out.pin

        init
            pin a
            pout a
        pinguim

        Contém um exemplo de código que realiza operações de leitura e impressão de valores.

##  condition.pin 

        init
            pin a
            b = 5
            pif (a==b) pegin
                pout "igual"
            pend
            paf {
                pout "diferente"
            }
        pinguim

        Contém um exemplo de código que demonstra uma estrutura condicional.

##  repetition.pin 

        init
            a = 5
            i = 0
            phile(i<a) { 
                pin b
                pout b
                i = i + 1
            pend
        pinguim

        Contém um exemplo de código que utiliza um loop para imprimir valores.

##  all.pin

        init
            a = 4
            b = 5
            pif (a==b) pegin
                pout "igual"
            pend
            paf pegin
                i = 0
                phile(i<=b) {
                    pout i
                    i = i + 1
                pend
            }
        pinguim

        Contém um exemplo de código que combina estruturas condicionais e de repetição.

# Arquivos de Saída (./output_txt/ -> XXXXXX_commands_output.txt, ./output_py -> XXXXX_translated.py, ./output_exe -> XXXXX.exe)

        Ao executar o script principal main.py, o analisador gera arquivos de saída que contêm as 
        DESCRIÇÕES DOS COMANDOS presentes nos exemplos de códigos analisados, as TRADUÇÕES desses 
        códigos para a linguagem de programação Python e os EXECUTÁVEIS de cada código. Cada arquivo 
        de entrada terá um arquivo de saída '.txt', um '.py' e outro .exe correspondentes, nomeados
        com o sufixo '_commands_output.txt' para as descrições e '_translated.py' para a tradução do 
        código. Esses arquivos de saída são gerados automaticamente durante o processo de compilação 
        e são salvos em diferentes diretórios (./output_txt, ./output_py, ./output_exe).

##  in_out_commands_output.txt

        INICIO DO PROGRAMA => init
        COMANDO DE ENTRADA => pin a
        COMANDO DE SAIDA => pout a
        FIM DO PROGRAMA => pinguim

        Correspondente ao arquivo de entrada 'in_out.txt'. Contém as DESCRIÇÕES DOS COMANDOS
        presentes no exemplo citado, que realiza operações de leitura e impressão de valores.
            
##  condition_commands_output.txt

        INICIO DO PROGRAMA => init
        COMANDO DE ENTRADA => pin a
        ATRIBUICAO => b = 5
        CONDICIONAL => pif (CONDICAO a == b)
        INICIO DO BLOCO => pegin
        COMANDO DE SAIDA => pout "igual"
        FIM DO BLOCO => pend
        DESVIO CONDICIONAL => paf
        INICIO DO BLOCO => {
        COMANDO DE SAIDA => pout "diferente"
        FIM DO BLOCO => }
        FIM DO PROGRAMA => pinguim

        Correspondente ao arquivo de entrada 'condition.txt'. Contém as DESCRIÇÕES DOS COMANDOS
        presentes no exemplo citado, que demonstra uma estrutura condicional.
        
##      repetition_commands_output.txt

        INICIO DO PROGRAMA => init
        ATRIBUICAO => a = 5
        ATRIBUICAO => i = 0
        COMANDO DE LOOP => (CONDICAO i < a)
        INICIO DO BLOCO => {
        COMANDO DE ENTRADA => pin b
        COMANDO DE SAIDA => pout b
        ATRIBUICAO => i = EXPRESSAO => i + 1
        FIM DO BLOCO => pend
        FIM DO PROGRAMA => pinguim

        Correspondente ao arquivo de entrada 'repetition.txt'. Contém as DESCRIÇÕES DOS COMANDOS
        presentes no exemplo citado, que utiliza um loop para imprimir valores.

##  all_commands_output.txt

        INICIO DO PROGRAMA => init
        ATRIBUICAO => a = 4
        ATRIBUICAO => b = 5
        CONDICIONAL => pif (CONDICAO a == b)
        INICIO DO BLOCO => pegin
        COMANDO DE SAIDA => pout "igual"
        FIM DO BLOCO => pend
        DESVIO CONDICIONAL => paf
        INICIO DO BLOCO => pegin
        ATRIBUICAO => i = 0
        COMANDO DE LOOP => (CONDICAO i <= b)
        INICIO DO BLOCO => {
        COMANDO DE SAIDA => pout i
        ATRIBUICAO => i = EXPRESSAO => i + 1
        FIM DO BLOCO => pend
        FIM DO BLOCO => }
        FIM DO PROGRAMA => pinguim

        Correspondente ao arquivo de entrada 'all.txt'. Contém as DESCRIÇÕES DOS COMANDOS presentes
        no exemplo citado, que combina operações de leitura e impressão de valores, estruturas 
        condicionais e de repetição.

##  in_out_translated.py

        a = input()
        print(a)

        Correspondente ao arquivo de entrada 'in_out.txt'. Contém a TRADUÇÃO do código que realiza 
        operações de leitura e impressão de valores.
            
##  condition_translated.py

        a = input()
        b = 5
        if (a == b):
            print("igual")
        else:
            print("diferente")

        Correspondente ao arquivo de entrada 'condition.txt'. Contém a TRADUÇÃO do código que demonstra 
        uma estrutura condicional.
        
##  repetition_translated.py

        a = 5
        i = 0
        while (i < a):
            b = input()
            print(b)
            i =  i + 1

        Correspondente ao arquivo de entrada 'repetition.txt'. Contém a TRADUÇÃO do código que utiliza 
        um loop para imprimir valores.

##  all_translated.py

        a = 4
        b = 5
        if (a == b):
            print("igual")
        else:
            i = 0
            while (i <= b):
                print(i)
                i =  i + 1

        Correspondente ao arquivo de entrada 'all.txt'. Contém a TRADUÇÃO do código que combina 
        operações de leitura e impressão de valores, estruturas condicionais e de repetição.
        
        

# Compilação e Execução (explicação mais detalhada do fluxo do código)

##  Tokenização

###     Lexer

            A tokenização é realizada pelo módulo lexer, que utiliza a biblioteca ply.lex para
            dividir o código fonte da linguagem Pinguim em tokens. Tokens são as menores unidades
            significativas do código, como palavras-chave, operadores, identificadores e literais.

###     Definição de Tokens

            Uma lista de tokens é definida, incluindo identificadores (ID), números (NUMBER, REAL), 
            strings (STRING), operadores (PLUS, MINUS, etc.), e palavras-chave reservadas (INIT, 
            PINGUIM, PIN, POUT, etc.).
        
###     Expressões Regulares

            Cada token é associado a uma expressão regular que descreve seu formato. Por exemplo, 
            t_PLUS = r'\+' define que o token PLUS corresponde ao caractere +.
        
###     Funções de Tokens

            Funções específicas são usadas para tokens com regras mais complexas, como t_ID, t_REAL, 
            t_NUMBER, e t_STRING. Essas funções também podem realizar ações adicionais, como conversão 
            de tipos.
        
###     Ignorar Espaços e Novas Linhas

            O lexer ignora espaços e tabulações (t_ignore = ' \t') e trata novas linhas para manter o 
            rastreamento do número de linhas (t_newline).
       
###     Tratamento de Erros

            Funções para tratamento de erros, como t_error, que lidam com caracteres ilegais no 
            código fonte.
        
###     Função tokenize_file()

            Esta função lê um arquivo de entrada, aplica o lexer para gerar tokens, e imprime os
            tokens no terminal.

##  Parsing

###     Parser

            O parsing é realizado pelo módulo myparser, que utiliza a biblioteca ply.yacc para analisar
            a estrutura gramatical do código fonte Pinguim e gerar uma representação interna (árvore de 
            análise sintática).

###     Definição da Gramática

            A gramática da linguagem Pinguim é definida usando regras p_*, que especificam como os 
            tokens devem ser combinados para formar estruturas sintáticas válidas. Por exemplo, 
            p_program, p_commands, p_command, p_assignment, etc.
        
###     Função p_program

            Define a estrutura básica de um programa Pinguim, que começa com INIT e termina com 
            PINGUIM. Comandos entre essas palavras-chave são processados pela regra commands.
        
###     Regras de Comandos

            Cada tipo de comando (atribuição, condicional, loop, entrada, saída, bloco) tem sua própria
            regra de análise. Por exemplo, p_assignment lida com atribuições, p_conditional lida com
            comandos condicionais PIF, e assim por diante.
        
###     Função de Erro

            A função p_error trata erros de sintaxe, fornecendo feedback sobre tokens inesperados ou
            problemas no código.
        
###     Função parse_file()

            Esta função realiza o parsing de um arquivo de entrada, armazenando descrições de comandos 
            em uma lista command_descriptions. Essas descrições são então escritas em um arquivo de 
            saída e traduzidas para Python.

## Tradução para Python

###     Módulo de Tradução

            O módulo translator é responsável por converter as descrições de comandos da linguagem 
            Pinguim em código Python.

###     Função translate_to_python

            Percorre a lista command_descriptions, traduzindo cada comando para sua equivalência em 
            Python. Utiliza indentação para representar a estrutura aninhada de blocos de código 
            (condicionais, loops, etc.).Adiciona palavras-chave e sintaxe Python (if, while, print, 
            etc.) conforme necessário.
        
###     Tratamento de Comandos

            Comandos de entrada (PIN) são traduzidos para input().
            Comandos de saída (POUT) são traduzidos para print().
            Comandos de atribuição, expressões, e blocos de código são manipulados para remover 
            informações desnecessárias e formatar corretamente em Python.
        
###     Criação de Arquivo Python

            A tradução é salva em um novo arquivo .py, que pode ser executado como um script Python.

## Geração de Executáveis

###     Função build_executable:

        Usa PyInstaller para criar um executável único a partir de um script Python.

###     Função generate_executables:

        Itera sobre todos os arquivos .py na pasta especificada, gerando um executável para cada um.

## Integração dos Componentes

        O código final mostra como todos esses componentes (tokenização, parsing, tradução e geração 
        de executáveis) são integrados para compilar programas escritos na linguagem Pinguim. Ele 
        assume uma estrutura de pastas específica e utiliza bibliotecas como ply e PyInstaller para 
        alcançar os objetivos de compilação e execução.

# Instalações

## Instalação do [Python](https://www.python.org/downloads/)

        Baixe e instale o Python a partir do site oficial. Certifique-se de adicionar o Python ao 
        PATH durante a instalação.

## Instalação da Biblioteca Ply

        Para instalar a biblioteca Ply, você pode usar o pip, que é o gerenciador de pacotes 
        do Python. Execute o seguinte comando no terminal:

            pip install ply

## Instalação do PyInstaller

        Para instalar o PyInstaller, você pode usar o pip, que é o gerenciador de pacotes 
        do Python. Execute o seguinte comando no terminal:

            pip install pyinstaller

# Requisitos

        Certifique-se de ter o Python 3.6 ou superior, a biblioteca Ply e o pyinstaller instalados 
        em seu sistema. Os arquivos 'main.py', 'lexer.py', 'myparser.py', 'translator.py', 'builder.py'
        e a pasta 'src_files' (que contém os arquivos: 'in_out.pin', 'condition.pin', 'repetition.pin'
        e 'all.pin') devem estar presentes no mesmo diretório.

##  Estrutura do Diretório ./CompiladorPinguim (antes de compilar)

        lexer.py
        myparser.py
        translator.py
        builder.py
        main.py

        ./src_files 

            in_out.txt 
            condition.txt 
            repetition.txt
            all.txt

##  Estrutura do Diretório ./CompiladorPinguim (depois de compilar)

        lexer.py
        myparser.py
        translator.py
        builder.py
        main.py

        ./src_files 

            in_out.pin 
            condition.pin
            repetition.pin
            all.pin

        ./__pycache__

            lexer.cpython-312.pyc
            myparser.cpython-312.pyc
            parsetab.cpython-312.pyc
            translator.cpython-312.pyc

        ./output_txt

            in_out_commands_output.txt
            condition_commands_output.txt
            repetition_commands_output.txt
            all_commands_output.txt

        ./output_py

            in_out_translated.py
            condition_translated.py
            repetition_translated.py
            all_translated.py
       
       ./output_exe 

            in_out.exe 
            condition.exe
            repetition.exe
            all.exe

# Comentários finais

        Mesmo não sendo nescessária essa documentação que de certa forma é exagerada, deixei
        desse jeito para postar no GitHub e treinar a formatar o README.md e os comandos git,
        como git push entre outros.

        Como o trabalho está sendo postado no GitHub, nos reservamos o direito de não nos 
        responsabilizarmos por cópias descaradas ou discretras do projeto, uma vez que, não temos 
        controle sobre o acesso dos outros grupos ao VSCode dos intregrantes que postarem.
