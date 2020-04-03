'''
10. Elabore o programa que leia a altura e o sexo (‘M’ pra masculino e ‘F’ pra feminino) de um grupo de pessoas e gere a tela de saída com as seguintes informações: maior altura do grupo, menor altura do grupo, média de altura das mulheres e a diferença percentual entre os homens e as mulheres.
'''

#declara as variáveis
qtd_m = 0
qtd_f = 0
menor_altura = 3
maior_altura = 0
alturas_m = 0
alturas_f = 0
print("digite 0 na altura para sair da repetição\n")
while(True):
    altura = float(input("Digite a altura: "))
    if(altura==0):
        break           
    #converte o texto digitado para maiúsculo
    sexo = input("Digite M ou F para o sexo: ").upper()    
    if(sexo == "M"):
        qtd_m = qtd_m + 1
        alturas_m = alturas_m + altura        
    if(sexo == "F"):
        qtd_f = qtd_f + 1
        alturas_f = alturas_f + altura
    #verifica se a altura digitada é maior que a maior
    if(altura>maior_altura):
        maior_altura = altura
    #verifica se a altura digitada é menor que a menor ou se a variável foi inicializada
    if(altura<menor_altura):
        menor_altura = altura
print("Maior altura:", maior_altura)
print("Menor altura:", menor_altura)
if qtd_m > 0:                      #evitar divisão por 0
    print("Porcentagem de homens: %.2f" %((qtd_m/(qtd_m+qtd_f))*100))
if qtd_f > 0:
    print("Média altura mulheres: %.2f" %(alturas_f/qtd_f))
    print("Porcentagem de mulheres: %.2f" %((qtd_f/(qtd_m+qtd_f))*100))