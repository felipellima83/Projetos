planetas = ["mercurio","venus","terra","marte","jupiter","saturno","urano","netuno","plutao"]
x="plutao"
planetas.pop(8)
print(planetas)

planetas.append(x)
print(planetas)
planetas.pop()
print(planetas)

planetas.insert(2,x)
print(planetas)
planetas.remove("plutao")
print(planetas)