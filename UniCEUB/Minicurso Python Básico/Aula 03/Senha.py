senha = int(input("Qual a senha: "))
while senha != 123:
    senha = int(input("Senha incorreta, digite novamente: "))
if senha == 123:
    print("Acesso garantido!")