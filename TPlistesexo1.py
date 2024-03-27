import random

def remplirListe(liste):
    for _ in range(0, 10):
        liste.append(random.randint(0, 101))

def valMax(liste):
    return max(liste)

def valMin(liste):
    return min(liste)


tab = []
remplirListe(tab)
print(tab)
print("Valeur max: ", valMax(tab))
print("Valeur min: ", valMin(tab))
