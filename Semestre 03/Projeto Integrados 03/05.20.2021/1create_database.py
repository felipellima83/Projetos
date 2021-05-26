"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

- Instalar o pacote mysql-connector-python:
Menu:
  File
    – settings
Project: NomeProjeto
    - Python Interpreter
Canto inferior esquerdo 	[ + ]
Available packages: ...
    mysql-connector-python
"""
# import mysql.connector
from mysql.connector import connect, Error
try:
    conexao = connect(host='localhost',     # host='127.0.0.1',
                      user='root',
                      password='spfc99',    # passwd='',
                      database='')
    print('Conexão:', conexao)
    db_info = conexao.get_server_info()     # Pega informações do servidor
    print("Connected to MySQL Server version:", db_info)
    cursor = conexao.cursor()               # Cria o cursor para executar os comando SQL
    cursor.execute("SHOW DATABASES")        # Mostra os database existentes
    print('- Show databases:')
    for x in cursor:
        print(x[0])                         # print(x)
    print('Qtd. databases:', cursor.rowcount)
    ''' Sintaxe:
        create database if not exists nome_database    '''
    sql = "CREATE DATABASE if not exists db_cadastro"  # db_cadastro é o nome do database
    cursor.execute(sql)
    cursor.execute("SHOW DATABASES")
    registros = cursor.fetchall()       # Lista de tuplas com os databases
    print('- Show databases:')
    print(registros)                    # Mostra ha horizontal
    print('Qtd. databases:', cursor.rowcount)
except Error as erro:                   # Executa se ocorreu algum erro
    print('Erro na conexão ou create database\n', erro)
else:
    cursor.close()
    conexao.close()
    print('\nConexão fechada.')
