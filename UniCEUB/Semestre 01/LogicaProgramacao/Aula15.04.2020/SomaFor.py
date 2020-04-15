soma=0
final = int(input("A soma termina em qual número? "))
for i in range(1, final + 1):
    if i%2==0:
        soma+=i
print(soma)