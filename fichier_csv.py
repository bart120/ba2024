import csv

fichier = open('movies.csv','r')
#ligne = fichier.readline()
#tab_ligne = ligne.split(',')
#print(tab_ligne)
tab = []
lignes = fichier.readlines()
for l in lignes:
    tab.append(l.split(','))
#print(tab)
print(tab[10][0])




