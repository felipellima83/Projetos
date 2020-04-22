def mediaTurma():  
    soma = 0
    media=0      
    while True:          
        try:
            qnt = int(input("Quantos alunos tem a turma? "))
            for i in range(qnt):
                nota = float(input(f"Digite a nota do {i+1}º aluno: "))
                soma+=nota
                i+=1
            media=soma/qnt
        except Exception as erro:
            print("A nota digitada não é um valor válido.", erro.__class__.__name__)
            continue
        else:
            return media
n1 = mediaTurma()
print(f"A média da turma foi de {n1:.2f}.")