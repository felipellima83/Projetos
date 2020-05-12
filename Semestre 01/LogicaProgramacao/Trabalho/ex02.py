ficar_em_casa = int(input("Considerando todo o período de isolamento social, quantos porcento do tempo você se isolou (0-100)? "))
if ficar_em_casa >= 95:
    print("Parabéns você está contribuindo muito para acabarmos com esse vírus!")
elif ficar_em_casa > 30 and ficar_em_casa < 95:
    usar_mascara = input("Quando você precisa sair de casa, você usa máscara (s ou n)? ")
    usar_mascara = usar_mascara.lower()
    if usar_mascara == "s":
        print("Tente se isolar mais e quando precisar sair use sempre máscara, assim você ajuda a reduzir a contaminação.")
    else:
        print("Use a máscara!!! Além de ser obrigatório, você ajuda a reduzir a contaminação.")
else:
    print("Fique em casa, a situação é séria!")
