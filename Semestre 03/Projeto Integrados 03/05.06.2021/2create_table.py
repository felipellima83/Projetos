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

- Na base de dados db_loja, Crie a tabela tb_produto comm as características de
um produto de uma loja:
O identificador, o nome do produto sem valores repetidos, o preço e a data de validade.
"""

# Mouse direito na pasta - Mark Directory as - Sources Root
# from Aula2.conexao import *
from funcoes import *

conexao = cria_conexao()
cursor = conexao.cursor()

# sql = "CREATE DATABASE if not exists db_loja"
# cursor.execute(sql)

sql = """ CREATE TABLE IF NOT EXISTS tb_produto(
    idt INT NOT NULL AUTO_INCREMENT,            # Atualiza automaticamente a chava primária
    nome VARCHAR(45) UNIQUE NOT NULL,           # Valores sem repetição
    preco DECIMAL(9,2) NOT NULL,
    dta_validade DATE NULL,
    PRIMARY KEY (idt)                           # Define a chave primária
    )   """
cursor.execute(sql)
cursor.close()
fecha_conexao(conexao)
