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
sql = '''
    select *
    from tb_funcionario
    '''
cursor.execute(sql)
registros = cursor.fetchall()       # Uma lista de tupla registros recebe os dados da tabela.
print("Quantidade de registros na tabela:", cursor.rowcount)
print('- List of tuplas:')                  # Solução 1
print(registros)
print('- Tuplas:')                          # Solução 2
for row in registros:
    print(row)
print("- Colunas, notação de vetor:")       # Solução 3
for row in registros:
    print("Idt:", row[0])
    print("Name:", row[1])
    print("Salário:", row[2])
print("- Colunas, nome coluna:")
for idt, nome, salario in registros:        # Solução 4
    print("Idt:", idt)
    print("Name:", nome)
    print("Salário:", salario)
cursor.close()
conexao.close()
print('\nConexão fechada.')

