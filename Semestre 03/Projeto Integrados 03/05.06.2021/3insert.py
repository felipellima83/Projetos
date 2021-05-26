"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.
"""
from funcoes import *

conexao = cria_conexao()

cursor = conexao.cursor()
qtd_registros(conexao)              # Quantidade de registros na tabela
sql = """
    insert into tb_produto
    (nome, preco, dta_validade)
    values     
    ('Arroz tipo 1', 30.00, '2021-11-17')        
    # ('Feijão', 10.00, '2022-05-23')        # Insere um de cada vez
    """
cursor.execute(sql)
print('Registros inseridos:', cursor.rowcount)  # Qtd. inseridos
conexao.commit()                    # Confirma a alteração no database
cursor.close()
fecha_conexao(conexao)
''' Insere mais de um registro.
sql = """
    insert into tb_produto
    (nome, preco, dta_validade)
    values     
    ('Arroz', 30.00, '2021-11-17'),
    ('Feijão', 10.00, '2022-05-23')    
    """

'''
