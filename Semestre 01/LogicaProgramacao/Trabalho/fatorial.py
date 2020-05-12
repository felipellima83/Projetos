def fatorial(n, show=False):

    fat = 1
    for c in range(n, 0, -1): #uso de For dentro da função fatorial()
        if show:
            print(c, end=' ')
        if c > 1:
            print(' x ', end=' ')
        else:
            print(' = ', end=' ')
        fat *= c
    return fat