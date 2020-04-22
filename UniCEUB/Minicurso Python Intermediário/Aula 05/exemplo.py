soma = 0
while True:
    try:
        alunos = int(input('Número de alunos da turma: '))
        for c in range(alunos):
            nota = float(input(f'Nota do aluno {c + 1}: '))
            soma += nota
        media = soma / alunos
    except ZeroDivisionError:
        print('Por favor, digite um número diferente de 0')
        continue
    except TypeError:
        print('Por favor, digite um número inteiro1: ')
        continue
    except ValueError:
        print('Por favor, digite um número inteiro: ')
        continue
    else:
        print("deu certo")
        break