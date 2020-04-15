soma=0
for i in range(1,31):
    x = 1/i
    i+=1
    soma+=x
    print(x)
print("A soma é igual a {:.5f}.".format(soma))