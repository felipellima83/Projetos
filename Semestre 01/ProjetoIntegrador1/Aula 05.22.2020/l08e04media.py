'''
4. Construa o programa que calcule a média aritmética de uma turma com trinta alunos,
onde cada aluno realizou uma avaliação. Além da média da turma, mostre também a tela
de saída tabular com o número e a nota dos alunos.
- Obs.: Para simplificar os testes, substitua trinta por três.
-----------------------------------------------------------------------------------
'''
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
'''
Alterações:
a. Não existe aluno zero, resolva este problema.
b. Em Python, podemos fazer o for iterar sobre uma lista qualquer. Refaça o segundo
for para iterar sobre a lista l_notas.
c. Na alteração anterior, mostre também o número do aluno.
d. Refaça sem usar o somador dentro do for.
e. Refaça usando uma função de lista no cálculo da média.
        DICAS:
for i in range(0, 3):                      # a.
    print( i + 1, ":", l_notas[i])
for nota in l_notas:                      # b.
    print(nota)
indice = 0                                     # c.
for nota in l_notas:                      
    print(indice, " - ", nota)
    indice = indice + 1
    #soma += valor                       # d.
# mostra a lista de notas
soma = sum (l_notas)
#print("A média é:", soma / 3)                    # e.
print("A média é:", soma / len (l_notas))
'''
