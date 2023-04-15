def verifie(tab):
    for i in range(1, len(tab)):
        if tab[i] < tab[i-1]:
            return False
    return True

verifie([0, 5, 8, 8, 9])

verifie([8, 12, 4])