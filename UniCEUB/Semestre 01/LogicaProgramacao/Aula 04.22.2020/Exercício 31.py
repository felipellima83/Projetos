print("Números Octais")
ct=0
for i in range(8):
    for j in range(8):
        for k in range(8):
           print(f"{ct} - {i}{j}{k}", end=", ")
           ct+=1
print(f"Foram reptidas {ct} vezes.")