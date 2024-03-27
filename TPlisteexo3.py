import random

def create_matrix(m, n):
    matrice = []
    for _ in range(0, n):
        ligne = []
        for _ in range(0, m):
            ligne.append(random.randint(-10, 10))
        matrice.append(ligne)
    return matrice

def display_screen(matrice):
    for ligne_mat in matrice:
        ligne_mat.sort()
        s = ""
        for val in ligne_mat:
            s = s + str(val) + " "
        print(s)

def display_screen_bis(matrice):
    for ligne_mat in matrice:
        coef = 1
        for val in ligne_mat:
            coef = coef * val
        if coef > 0 : 
            print("+")
        elif coef < 0:
            print("-")
        else:
            print("o")

mat = create_matrix(8, 7)
display_screen(mat)
display_screen_bis(mat)
