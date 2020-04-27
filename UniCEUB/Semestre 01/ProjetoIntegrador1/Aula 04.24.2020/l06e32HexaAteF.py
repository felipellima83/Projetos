'''
32
Implemente o programa que mostre a sequência dos números hexadecimais até F.
O sistema hexadecimal utiliza estes 16 símbolos:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E e F.
'''

for i in range(16):
    if (i<10):
        print(i)
    elif(i==10):
        print('A')
    elif(i==11):
        print('B')
    elif(i==12):
        print('C')
    elif(i==13):
        print('D')
    elif(i==14):
        print('E')
    else:
        print('F')

     

'''
a- Obtenha o mesmo resultado sem usar if, crie a lista
R:
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']:
   print(i)



'''
        

    
