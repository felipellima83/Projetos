"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.
"""
from funcoes import *

conexao = cria_conexao()

cursor = conexao.cursor()

# qtd_registros(conexao)
mostra_registros(conexao)

sql = """
    insert into tb_produto
    (nome, preco, dta_validade)
    values (%s, %s, %s) 
    """
lista = [('Leite', 6.00, '2021-11-13'),
         ('Café', 14.00, '2022-02-22')]

# Use the cursor’s executemany() function to insert multiple records into a table.
cursor.executemany(sql, lista)      # (cmd_sql, list)
print('Registros inseridos:', cursor.rowcount)
conexao.commit()            # Confirma a alteração no database
cursor.close()
fecha_conexao(conexao)
''' ----- ALTERAÇÃO:
a. Inserir os dados nas tuplas e na lista usando o input, permitir que o usuário 
digite vários registros e no final digite <enter>.
    ----- DICAS:


lista = list()
print('Digite <enter> para sair')
while True:
    p_nome = input('Nome: ')
    if p_nome == '':
        break
    p_preco = float(input('preço: '))
    p_data = input('aaaa-mm-dd: ')
    tupla = (p_nome, p_preco, p_data)
    # print(tupla)
    lista.append(tupla)
# print(lista)
'''
