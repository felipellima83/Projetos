def compara_valores (a,b):
    if a == b:
        ret = 0
    elif a > b:
        ret = 1
    else:
        ret = -1
    return ret

if __name__ == "__main__":
    print(compara_valores(float(input("Qual número? ")),float(input("Qual número? "))))