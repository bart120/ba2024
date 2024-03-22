def est_pair(nombre):
    # % (modulo) permet d'obtenir le reste d'une division
    test = (nombre % 2) == 0 
    return test


def est_dans_tableau(tab, element):
    for e in tab :
        if e == element:
            return True
    return False

def afficher_tableau(tab):
    for e in tab:
        print(e)