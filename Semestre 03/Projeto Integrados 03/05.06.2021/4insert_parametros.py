"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.
"""
from funcoes import *
conexao = cria_conexao()

cursor = conexao.cursor()

qtd_registros(conexao)

sql = """
    insert into tb_produto
    (nome, preco, dta_validade)
    values (%s, %s, %s)
    """
a_nome = input('Nome: ')
a_preco = float(input('Preço: '))
a_data = input('aaaa-mm-dd: ')

cursor.execute(sql, (a_nome, a_preco, a_data))  # Parênteses obrigatórios (cmd_sql, (tupla))

print('Registros inseridos:', cursor.rowcount)
conexao.commit()                    # Confirma a alteração no database
cursor.close()
fecha_conexao(conexao)
'''
tupla = (p_nome, p_preco, p_data)
cursor.execute(sql, tupla)


'''
