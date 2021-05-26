"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

"""

from funcoes import *
try:
    conexao = cria_conexao()
    cursor = conexao.cursor()
    qtd_registros_cargo(conexao)                # Inserir na tabela tb_cargo
    ''' Sintaxe:
        insert into nome_tabela
        (nome_coluna1, nome_coluna2, ..., nome_colunan)
        values (%s, %s, ..., %s)                        '''
    # Inserir primeiro os dados na tabela domínio, td_cargo
    sql = """
        insert into td_cargo
        (nome)                      
        values (%s)                                     """
    a_nome = input('Nome do cargo: ')
    cursor.execute(sql, (a_nome, ))  # Parênteses obrigatórios (cmd_sql, (tupla))
    conexao.commit()                    # Confirma a alteração no database
    print('Registros inseridos:', cursor.rowcount)
    qtd_registros_empregado(conexao)            # Inserir na tabela tb_empregado
    sql = """
        insert into tb_empregado
        (nome, dta_nascimento, genero, cod_cargo)
        values (%s, %s, %s, %s)                     """
    a_nome = input('Nome empregado: ')
    a_dta_nascimento = input("Data nascimento (aaaa-mm-dd): ")
    a_genero = input("Gênero [M] ou [F]:")
    a_cod_cargo = input('Código Cargo: ')
    tupla = (a_nome, a_dta_nascimento, a_genero, a_cod_cargo)  # Cria tupla com dados
    cursor.execute(sql, tupla)
    print('Registros inseridos:', cursor.rowcount)
    conexao.commit()                    # Confirma a alteração no database
except Error as erro:
    print('Erro no insert.\n', erro)
else:
    cursor.close()
    fecha_conexao(conexao)

'''
tupla = (p_nome, p_preco, p_data)
cursor.execute(sql, tupla)
---
1	Presidente
2	Gerente
3	Analista
4	Desenvolvedor
5	Suporte
6	Vendedor
---
except Error as erro:
    print('Erro no insert.\n', erro)
    conexao.rollback()

'''
