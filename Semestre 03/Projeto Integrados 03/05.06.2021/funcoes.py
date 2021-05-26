"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha. """
import mysql.connector
def cria_conexao():
    conexao = mysql.connector.connect(user='root',
                                      password='spfc99',
                                      host='127.0.0.1',      # host='localhost',
                                      database='db_loja')
    print('Conexão:', conexao)
    return conexao
def fecha_conexao(con):
    con.close()
    print('\nConexão fechada.')
def qtd_registros(con):
    cursor = con.cursor()
    sql = ''' select * from tb_produto '''
    cursor.execute(sql)
    registos = cursor.fetchall()
    print("Registros na tabela:", cursor.rowcount)
def mostra_registros(con):
    cursor = con.cursor()
    sql = ''' select * from tb_produto   '''
    cursor.execute(sql)
    registros = cursor.fetchall()
    print('- Registros:')
    # for row in registros:                         # Na horizontal no formato de tupla
    #     print(row)
    for idt, nome, preco, dta_validade in registros:
        print(f'{idt}, {nome}, {preco}, {dta_validade}')  # Na horizontal com f-string
    qtd_registros(con)
