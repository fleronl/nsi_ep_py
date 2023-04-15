def recherche(tab, n):
    indice_solution = len(tab)
    for i in range(len(tab)):
        if tab[i] == n:
            indice_solution = i
    return indice_solution

# Testez votre algorithme
try:
    assert recherche([5, 3],1) == 2
    assert recherche([2,4],2) == 0
    assert recherche([2,3,5,2,4],2) == 3
    print('Tout semble correct 👍')
    
except AssertionError as asser:
    print('Le résultat de votre fonction n\'est pas conforme 🤔')