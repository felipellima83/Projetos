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
	mysql-connector-python                  """
import mysql.connector
conexao = mysql.connector.connect(user='root',
                                  password='spfc99',
                                  host='127.0.0.1',
                                  database='db_empresa')
print('Conexão:', conexao)
cursor = conexao.cursor()
# sql = "CREATE DATABASE if not exists db_empresa"
# cursor.execute(sql)
sql = """ 
    CREATE TABLE IF NOT EXISTS tb_funcionario(
    idt INT NOT NULL,
    nome VARCHAR(45) NOT NULL,
    salario DECIMAL(9,2) NULL,
    PRIMARY KEY (idt)
    )   """
cursor.execute(sql)
conexao.close()
print('\nConexão fechada.')
