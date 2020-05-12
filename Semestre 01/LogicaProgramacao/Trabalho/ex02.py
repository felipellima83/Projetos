ficar_em_casa = int(input("Quantos porcento você tem praticado de isolamento social? "))
if ficar_em_casa == 100:
    print("Parabéns você está contribuindo muito para acabarmos com esse vírus!")
elif ficar_em_casa == 50:
    usar_mascara = input("Quando você precisa sair de casa, você usa máscara (s ou n)? ")
    usar_mascara = usar_mascara.lower()
    if usar_mascara == "s":
        print("Isso mesmo, use sempre máscara antes de sair de casa, assim você ajuda a reduzir a contaminação.")
    else:
        print("Use a máscara!!! Além de ser obrigatório, você ajuda a reduzir a contaminação.")
else:
    print("Fique em casa, a situação é séria!")
