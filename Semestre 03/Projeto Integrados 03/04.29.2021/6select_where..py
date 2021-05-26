"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.
"""
import mysql.connector
conexao = mysql.connector.connect(user='root',
                                  password='spfc99',
                                  host='localhost',             # host='127.0.0.1',
                                  database='db_empresa')
print('Conexão:', conexao)
cursor = conexao.cursor()
sql = '''
    select *
    from tb_funcionario
    where idt = 1
    # where nome_coluna = valor     (sintaxe)
    # where nome = 'Alice'
    # where salario > 3000
    '''
cursor.execute(sql)
registros = cursor.fetchall()
print("Registros na consulta:", cursor.rowcount)
print('- List of tuplas:')
print(registros)
print('- Tuplas:')
for row in registros:
    print(row)
cursor.close()
conexao.close()
print('Conexão fechada.')

