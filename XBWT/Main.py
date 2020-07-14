from . import XBWT
from . import Recherche
from . import Fonctions
from . import BWT
import time


""" Fonction qui construit la liste des noeuds internes, la chaine s (paramètre avec lequelle on 
    calcule la bwt et on calcule la longueur de cette chaine s.
"""
def saisirMotifs(motifs):
    # On copie les motifs
    chaineOriginale = motifs.copy()
    # On inverse chaque motif
    for i in range(len(chaineOriginale)):
        chaineOriginale[i] = chaineOriginale[i][::-1]
    # On constuit la table des noeuds internes qui contient tous les noeuds
    listeDesNoeuds = sorted(chaineOriginale.copy())
    # On construit la chaine sur laquelle on effectue les recherches, qu'on nomme chaine originale
    chaineOriginale = "$".join(chaineOriginale)
    chaineOriginale = chaineOriginale + "$"
    # On enregistre la longueur de la chaine
    longChaineOriginale = len(chaineOriginale)
    return chaineOriginale, listeDesNoeuds, longChaineOriginale

def methodeXbwt(motifs, text):
    global ll, chaineDesParentheses, listeDesNoeuds, f, tempsConstruction, temps
    debutTout = time.time()
    chaineOriginale, listeDesNoeuds, longChaineOriginale = saisirMotifs(motifs)
    suffixArr = BWT.suffixArray(chaineOriginale, longChaineOriginale)
    bwt = BWT.calculerBwt(suffixArr, chaineOriginale)
    rcp, lcp = XBWT.calculerRcpLcp(longChaineOriginale, chaineOriginale, suffixArr)
    mr = XBWT.calculerMr(longChaineOriginale, rcp, lcp)
    ll = XBWT.calculerXbwt(mr, longChaineOriginale, bwt)
    chaineDesParentheses = XBWT.calculerP(rcp, mr, longChaineOriginale, chaineOriginale, suffixArr)
    occ = Fonctions.construireOcc(ll)
    f = Fonctions.construireF(occ, ll)
    listeDesNoeuds = XBWT.construireListeDesNoeudsFinaux(ll, listeDesNoeuds)
    results = Recherche.recherche(text, chaineDesParentheses, listeDesNoeuds, f, ll)
    finTout = time.time()

    temps = finTout - debutTout
    return results



