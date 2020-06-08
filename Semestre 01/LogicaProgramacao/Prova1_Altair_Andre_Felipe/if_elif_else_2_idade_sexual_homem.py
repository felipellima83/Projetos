#Curso: Ciência da Computação
#Professor: Antônio Barbosa Junior
#Disciplina: Lógica de programação
#Alunos: Altair Correia Azevedo, André Luiz Vieira Mostaro e Felipe Ferreira Lima e Lima

# If, elif e else 02
# IDADE SEXUAL DO HOMEM - este programa recebe a idade do usuário e retorna duas informações a respeito
idade = int(input("Qual a fase do homem que você quer descobrir? "))
if idade <= 11:
    print("Essa pessoa está na fase da infância. No estágio:")
    if idade < 2:
        print("Mandruva. Comer, dormir e cagar.")
    elif idade > 2 and idade < 3:
        print("'Maratonista'.")
    elif idade > 3 and idade < 7:
        print("Do tudo 'Porquê?'.")
    else:
        print("Querendo ser gente.")
elif idade >=12 and idade <=20:
    print("Essa pessoa está na fase da adolescência. No estágio:")
    if idade >=12 and idade <=14:
        print("Já se acha grande para tomar banho sozinho.")
    elif idade >=15 and idade <=17:
        print("Tem certeza que já é adulto.")
    else:
        print("Cadê meu carro?!?!?!?")
elif idade >=21 and idade <60:
    print("Essa pessoa está na fase adulta. No estágio:")
    if idade >=21 and idade <=35:
        print("Qual a balada de hoje?")
    elif idade >=36 and idade <50:
        print("Como era bom ser criança, nossa responsabilidade era só estudar.")
    else:
        print("Síndrome do ninho vazio.")
else:
    print("Essa pessoa está na fase da idosa. No estágio:")
    if idade >60 and idade <70:
        print("Ai que dor!")
    elif idade >=70 and idade <80:
        print("Acho que estou ficando velho.")
    elif idade >=80 and idade <90:
        print("Terceira idade que nada, já estou é na quarta idade.")
    else:
        print("Matusalém.")