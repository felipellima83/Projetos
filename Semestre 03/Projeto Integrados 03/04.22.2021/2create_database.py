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

import mysql.connector

conexao = mysql.connector.connect(user='root',
                                  password='spfc99',
                                  host='127.0.0.1',
                                  database='')
print('Conexão:', conexao)

cursor = conexao.cursor()       # Cria o cursor para executar os comando SQL
sql = "CREATE DATABASE if not exists db_empresa"    # db_empresa é o nome do database (você escolhe)
cursor.execute(sql)

conexao.close()
print('\nConexão fechada.')
