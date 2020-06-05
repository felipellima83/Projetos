'''
14. Elabore o programa que apaga um valor do vetor. O usuário fornecerá a posição do vetor que o dado deverá ser apagado. Não deixe essa posição vazia, movimente os próximos valores.
Não utilize função especifica, faça esta manipulação através de lógica.
'''
import random

lista=[]
elementos = 10
for i in range(0,elementos):
    lista.append(random.randint(0,20))
print(lista)

pesquisa = int(input("Qual posição retirar? "))
if pesquisa >= elementos:
    print("Posição não existe nessa lista.")
else:
    lista.pop(pesquisa)
    print(lista)

    










'''ALTERAÇÕES:
a. Adicione uma condição. Se a posição que ele digitar for maior que o número de posições do vetor, mostrar a mensagem "Posição inválida"
b. Use o método pop() para remover um elemento do vetor.
'''

