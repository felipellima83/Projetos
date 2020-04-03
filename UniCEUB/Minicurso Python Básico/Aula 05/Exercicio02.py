#Curso: Minicurso de Python Básico
#Data: 03/04/2020

#Exercício 02
result=0
i2=0
for i in range(100, -1, -1):
    if i % 2 != 0 and i % 3 == 0:
        result+=i 
        i2+=1   
print("A soma de todos os {} encontrados é igual {}.".format(i2,result))