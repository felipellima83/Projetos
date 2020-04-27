'''
36. Elabore o programa que calcule n! (fatorial de n). O usuário fornecerá o valor inteiro “ n ”.
      Sabemos que: 	n! =  n  x  (n-1)  x  . . .  x  5  x  4  x  3  x  2  x  1;
		0! =  1, por definição.                              1! = 1

'''
produto = 1
i = 0
qnt = int(input("Qual número a ser fatorado? "))
for x in range(1,qnt+1):    
    produto*=x
    i+=1
print(f"O produto de todos os {i} digitados é: ", produto)


   
