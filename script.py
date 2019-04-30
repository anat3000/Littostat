with open("dicofr.txt", "r") as file_dico:
    dico = file_dico.read().split("\n")

with open("combis/4lettres.txt", "r") as file_combis:
    combis = file_combis.read().split("-")

combis_existantes = []

for combi in combis:
    if combi in map((lambda x: x.upper()), dico):
        combis_existantes.append(combi)

with open("results/4lettres.txt", "w") as f:
    print("Nombre de combinaisons existantes :", len(combis_existantes), file=f)
    print("Ratio de mots existants parmi les combinaisons :", (len(combis_existantes)/len(combis))*100, "%", file=f)
    print("Mots existants :", end='', file=f)
    for i in combis_existantes:
        print(i + " - ", end='', file=f)

print("Terminated !\nSaved in results/4lettres.txt")