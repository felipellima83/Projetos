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
sql = """
    insert into tb_funcionario
    (idt, nome, salario)
    values
    (1, 'Alice', 3000.00)           
    """
# (2, 'Rogério', 4000.00)
cursor.execute(sql)

conexao.commit()            # Confirma a alteração no database

conexao.close()
print('\nConexão fechada.')




'''
sql = """
    insert into tb_funcionario
    (idt, nome, salario)
    values
    (2, 'Rogério', 4000.00)
    """

sql = """
    insert into tb_funcionario
    (idt, nome, salario)
    values
    (1, 'Alice', 3000.00),
    (2, 'Rogério', 4000.00)    
    """
'''

