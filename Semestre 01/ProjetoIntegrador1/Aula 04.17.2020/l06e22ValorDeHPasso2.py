'''
22
Prepare o programa que calcule o valor de H, sendo que ele é determinado
pela série:
H = 1 + 3 + 5 + 7 + . . . + 99
   --  --  --   --         ----
    1   2   3   4           50

dica: numerador irá incrementar de 2 a 2 numeros
      denumerador irá incrementar de 1 a 1 numero

    onde: numerador         numerador
          ---------    +    ---------
          denumerador       denumerador
'''


#sintaxe do range: range( inicial , final + 1, passo)
#o range retorna uma lista
   
numerador = int(input("Qual o valor numerador? "))
denominador = int(input("Qual o valor denominador? "))
soma=0
for i in range(1, denominador+1):    
    soma+= numerador/i
    numerador+=2    
print("A soma é igual a {:.2f}.".format(soma))