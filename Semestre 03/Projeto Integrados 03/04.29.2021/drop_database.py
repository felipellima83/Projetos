import mysql.connector
conexao = mysql.connector.connect(user='root',
                                  password='spfc99',
                                  host='127.0.0.1',
                                  database='db_empresa')
print('Conexão:', conexao)
cursor = conexao.cursor()
sql = 'show databases'
cursor.execute(sql)
registro = cursor.fetchall()
print('- show databases: list of tuplas')
print(registro)
print('Qtd.:', cursor.rowcount)
print('- show databases: tuplas')
for x in registro:
    print(x)
print('Qtd.:', cursor.rowcount)
# sql = "drop database db_empresa"      # Não retire o comentário
# cursor.execute(sql)
sql = 'show databases'
cursor.execute(sql)
registro = cursor.fetchall()
print('- show databases: list of tuplas')
print(registro)
print('Qtd.:', cursor.rowcount)
conexao.close()
print('\nConexão fechada.')
