import random
soma = 0
a=0
b=0
c=0
d=0
e=0
f = 0
for i in range(60):
    x = random.randint(1,6)
    soma+=x
    print(x, end =" ")
    if x == 1:
        a+=1
    if x == 2:
        b+=1
    if x ==3:
        c+=1
    if x == 4:
        d+=1
    if x == 5:
        e+=1
    if x == 6:
        f+=1
print("\nSoma = ", soma, "nº 1 = ", a, "nº 2 = ", b, "nº 3 = ", c, "nº 4 = ", d, "nº 5 = ", e, "nº 6 = ",f, "\n", a/60*100,b/60*100,c/60*100,d/60*100,e/60*100,f/60*100)