def tabuada(num):

    for x in range(1,10):
        print(num,'+',x,'=',num+x, end='')
        print('\t',num,'-',x,'=',num-x, end='')
        print('\t',num,'*',x,'=',num*x, end='')
        print('\t',num,'/',x,'= %.2f'%(num/x))

num = int(input('Insira um número: '))
tabuada(num)


