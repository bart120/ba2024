from TPlistesexo1 import remplirListe

def permuter(liste, i, j):
    liste[i], liste[j] = liste[j], liste[i]

def trierListe(liste):
    liste.sort()


tab = []
remplirListe(tab)
print(tab)
permuter(tab, 1, 3)
print(tab)
trierListe(tab)
print(tab)