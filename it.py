from base import est_pair, est_dans_tableau, afficher_tableau


tab_fruits = ["kiwi", "mangue", "orange", "fraise"]
print(est_dans_tableau(tab_fruits, "kiwi"))
afficher_tableau(tab_fruits)


""" tableau = 34, 67, 128, 456, 2
print(tableau[2]) # affiche la valeur de la 3eme ligne du tableau
index  = 0
while index < len(tableau):
    print(tableau[index])
    index += 1 # index = index + 1

nb_impair = 0
nb_pair = 0
for num in tableau:
    #print(est_pair(num))
    if est_pair(num):
        nb_pair+=1
    else:
        nb_impair+=1
print("{} nombre(s) pair".format(nb_pair))
print("{} nombre(s) impair".format(nb_impair))

print(est_dans_tableau(tableau, 34))
 """