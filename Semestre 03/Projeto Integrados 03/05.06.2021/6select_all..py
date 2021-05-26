"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha. """
from funcoes import *
conexao = cria_conexao()
cursor = conexao.cursor()
sql = ''' select * from tb_produto '''
cursor.execute(sql)
registros = cursor.fetchall()           # registros é uma lista de tuplas
print('- List of tuplas:')
print(registros)                        # Mostra os registros na horizontal
print('- Tuplas:')
for row in registros:
    print(row)                          # Mostra os registros na veritical
print("- Colunas, notação de vetor:")
for row in registros:
    print("Idt:", row[0])
    print("Name:", row[1])
    print("Preço:", row[2])
    print('Data de validade:', row[3])
print("- Colunas, nome coluna:")
for idt, nome, preco, dta_validade in registros:
    print("Idt:", idt)
    print("Name:", nome)
    print("Preço:", preco)
    print('Data de validade:', dta_validade)
print('Registros na tabela:', cursor.rowcount)
# qtd_registros(conexao)
cursor.close()
fecha_conexao(conexao)
