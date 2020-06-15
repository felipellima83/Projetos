'''
Veja os vídeos abaixo:
video1 - Introdução a Listas
https://www.youtube.com/watch?v=YeaB5IgS2rY&index=25&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe
video2 - Listas dentro de listas, Adicionar novos elemetos a listas(append) 
https://www.youtube.com/watch?v=zzRiX_nIIMc&index=26&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe
'''

#função especifica para ler uma lista
def ler_lista(vetor, m):    #recebe como paramwtros:
    for i in range(tamanho_lista_alunos):              m
        print(f"[ {i} ] : {vetor[i]}") #imprime a posição do vetor e seu valor

def criar_lista (vetor,n):
    for i in range(m):
        valor = int(input(f"Digite o {i+1}º número: "))
        lista_alunos.append(valor)
    print(lista_alunos)
    
def alunos_aprovados (vetor,qnt):
    criar_lista(lista_alunos,tamanho_lista_alunos)
    ler_lista(lista_alunos,tamanho_lista_alunos)
    ct=0
    for i in range(qnt):
            nota = int(input(f"Digite a nota do {i+1}º número: "))
            if nota > 5:
                lista_alunos.append(nota)
                ct+=1
    print(f"Foram aprovados {ct} alunos.")

#inicio do código
if __name__ == "__main__":
    lista_alunos = []
    tamanho_lista_alunos = int(input("Quantos alunos? "))
    alunos_aprovados(lista_alunos,tamanho_lista_alunos)

'''
Alterações:
a. Criar uma lista de tamanho "m", fornecido pelo usuário.

b. utilizar a função "funcao_ler_Lista" para ler todos os valores da lista.

Dica: utilizar o comando "len(l_valores)" para receber o tamanho da lista.

c. Criar uma função para "escrever_lista" na lista/vetor, chamar a função
para preencher cada posição da lista

Dica:
def escrever_lista(nome_vetor,tamanho):
      script(código da função)
      utilizar a metodo append(valor) para adicionar valores a lista/vetor

d. Utilizar as funções criadas anteriormente para construir um função chamada
"Numero_Aprovados".

Esta função deverá ter como parametros de entrada, a quantidade de alunos digitados
pelo usuario; Construir um vetor de notas dos alunos;
Imprimir estas notas utilizando a "funcao_ler_lista";
E mostrar a quantidade de alunos acima de 5.0.

'''
