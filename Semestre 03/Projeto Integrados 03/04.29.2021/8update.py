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
sql = ''' select * from tb_funcionario '''              # Mostra todos antes
cursor.execute(sql)
registros = cursor.fetchall()
print("Quantidade de registros na tabela:", cursor.rowcount)
print('- List of tuplas:')
print(registros)
sql = '''                                               # Atualiza
    update tb_funcionario
    set salario = 4200.00
    where nome = 'Rogerio'
    '''
cursor.execute(sql)
print("Registros atualizados:", cursor.rowcount)
conexao.commit()
sql = ''' select * from tb_funcionario '''              # Mostra todos depois
cursor.execute(sql)
registros = cursor.fetchall()
print("\nQuantidade de registros na tabela:", cursor.rowcount)
print('- List of tuplas:')
print(registros)
cursor.close()
conexao.close()
print('\nConexão fechada.')