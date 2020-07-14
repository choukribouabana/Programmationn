from . import Navigation
from . import Fonctions

# Cette fonction détermine l'intervalle des symboles sortant du noeud donné
def calculerIntervalle(indiceNoeud, ll):
    # Le début est la position du indiceNoeud ième 1 dans ll +1 ou 0 si le noeud est la racine
    debut = 0 if indiceNoeud == 0 else Fonctions.select(1, ll, indiceNoeud) + 1
    # La fin est la position de (indiceNoeud+1)ième 1 dans ll
    fin = Fonctions.select(1, ll, indiceNoeud + 1)
    return ll[debut:fin]


# Cette fonction vérifie si le noeud correspond à un état final
def noeudFinal(indiceNoeud, symbolsSortants, results, listeDesNoeuds, i):
    # Si ll[debut:fin] contient "$" alors c'est un état final
    if "$" in symbolsSortants:
        results.append(((listeDesNoeuds[indiceNoeud][::-1]), i - len(listeDesNoeuds[indiceNoeud]) + 1))


# Fonction de recherche
def recherche(text, chaineDesParentheses, listeDesNoeuds, f, ll):
    results = list()
    indiceNoeud = 0
    # On lit les caractères du text un par un
    for i, symbol in enumerate(text):
        # On enregistre les symboles sortants du noeud actuel
        symbolsSortants = calculerIntervalle(indiceNoeud, ll)
        # Si le noeud actuel est différent de la racine et
        # il existe un chemin depuis le noeud actuel en suivant le symbole actuel
        while indiceNoeud != 0 and symbol not in symbolsSortants:
            # On revient au plus long préfixe
            indiceNoeud = Navigation.trouverLePlusLongSuffixe(indiceNoeud, chaineDesParentheses)
            symbolsSortants = calculerIntervalle(indiceNoeud, ll)
        # Si un chemin existe alors on passe au noeud suivant
        if symbol in symbolsSortants:
            indiceNoeud = Navigation.noeudSuivant(indiceNoeud, symbol, f, ll)
        # Sinon si aucun chemin n'existe on passe au caractère suivant du texte
        else:
            continue
        indiceNoeudTmp = indiceNoeud
        # Pour chaque noeud on vérifie tous ses suffixes
        while indiceNoeudTmp != 0:
            symbolsSortants = calculerIntervalle(indiceNoeudTmp, ll)
            noeudFinal(indiceNoeudTmp, symbolsSortants, results, listeDesNoeuds, i)
            indiceNoeudTmp = Navigation.trouverLePlusLongSuffixe(indiceNoeudTmp, chaineDesParentheses)
    return results