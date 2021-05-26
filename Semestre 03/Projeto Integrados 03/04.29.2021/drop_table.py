"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.
"""
import mysql.connector
conexao = mysql.connector.connect(user='root',
                                  password='spfc99',
                                  host='127.0.0.1',
                                  database='db_empresa')
print('Conexão:', conexao)
cursor = conexao.cursor()
sql = 'show tables'
cursor.execute(sql)
registro = cursor.fetchall()
print('- show tables: list of tuplas')
print(registro)
print('- show tables: tuplas')
for x in registro:
    print(x)
# sql = "drop table tb_funcionario"     # Não retire o comentário
# cursor.execute(sql)
sql = 'show tables'
cursor.execute(sql)
registro = cursor.fetchall()
print('- show tables: list of tuplas')
print(registro)

conexao.close()
print('Conexão fechada.')
