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
''' Obs.: o nome do diretório e dos arquvios .py não podem ter espaços e nem hífen, 
se precisar use underlline.             '''
# Mouse direito na pasta - Mark Directory as - Sources Root
# from Aula3.funcoes import *


from funcoes import *
import mysql.connector
conexao = mysql.connector.connect(user='root',
                                  password='spfc99',
                                  host='localhost',     # host='127.0.0.1',
                                  database='')
print('Conexão:', conexao)

cursor = conexao.cursor()           # Cria o cursor para executar os comando SQL
# sql = "CREATE DATABASE if not exists db_loja"  # db_loja é o nome do database (você escolhe)
# cursor.execute(sql)
cursor.close()
fecha_conexao(conexao)
