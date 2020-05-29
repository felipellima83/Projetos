'''
- 4. Construa o programa que calcule a média aritmética de uma turma com trinta alunos,
onde cada aluno realizou uma avaliação. Além da média da turma, mostre também a tela
de saída tabular com o número e a nota dos alunos.

l_notas = [ ]                          # lista de notas inicialmente vazia
soma = 0                              # valor da soma inicialmente zero
for i in range(0, 3):               # Repete 3 vezes
    valor = int(input("Digite a nota do aluno: ")) # recebe a nota
    l_notas.append(valor)                                   # adiciona à lista
    soma = soma + valor                                    # soma += valor                                                
# mostra a lista de notas
print ('Número - nota')
for i in range(0, 3):
    print(i, ":", l_notas[i])
# mostra a média
media = soma / 3
print("A média é:", media)

- 5. Refaça o programa anterior para mostrar também a quantidade de notas acima da
média da turma. 
- Obs.: Para simplificar os testes, substitua trinta por três.
'''
l_notas = [ ]                                               # lista de notas inicialmente vazia
soma = 0                                                    # valor da soma inicialmente zero
alunos = int(input("Quantos alunos tem na turma? "))        # define qnts elementos tem na lista
# for para inserir as notas dos alunos                           
for i in range(0, alunos):                                       # Repete 3 vezes
    valor = int(input(f"Digite a nota do {i+1} aluno: "))   # recebe a nota
    l_notas.append(valor)                                   # adiciona à lista
    soma = soma + valor                                     # soma += valor
print ('Aluno / Nota')                                     # imprime cabeçalho
# repetição para imprimir a posição e as notas dos alunos
for i in range(0, alunos):                                       # repete 3 vezes
    print(i, "/", l_notas[i])                               # imprime posição do aluno na lista e sua nota
media = soma / 3                                            # calcula a média da turma
print(f"A média da turma, com {len(l_notas)} alunos, é:", media)    # mostra a média da turma
ct = 0                                                      # contador das notas acima da média da turma
# mostra quantas notas foram acima da média da turma
for i in l_notas:                                           # repete de acordo com a qnt de elementos da lista
    if i > media:                                           # verifica se a nota é maior que a média
        ct+=1                                               # contador de notas acima da média da turma
print(f"Foram {ct} notas acima da média da turma.")         # imprime a qnt de notas acima da média da turma
'''
Alterações:

 
'''
