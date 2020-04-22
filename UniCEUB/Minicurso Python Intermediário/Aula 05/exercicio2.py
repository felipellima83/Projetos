print("*** Programa para calcular a média de uma turma! ***")
soma = 0

while True:
    try:
        qtdAlunos = int(input("Informe a quantidade de alunos da turma: "))
        for c in range(qtdAlunos):
            nota = float(input(f"Nota do aluno {c + 1}: "))
            soma += nota

        media = soma / qtdAlunos
    except ValueError as erro:
        print(f"\033[31mERRO ({erro.__class__.__name__}): Informe um valor inteiro.\33[m")
        continue
    except ZeroDivisionError as erro:
        print(f"\033[31mERRO ({erro.__class__.__name__}): Informe uma quantidade de alunos maior que zero.\33[m")
        continue
    else:
        print(f"\033[32mA média da turma é {media:.1f}")
        break
