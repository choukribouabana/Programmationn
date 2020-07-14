from . import Fonctions
import time

def methodeTrie(motifs, text):
	global kwtree, temps
	debutTout = time.time()
	# Nous créons le trie
	kwtree = Fonctions.KeywordTree(case_insensitive=True)
	# Nous ajoutons les motifs un par un
	for motif in motifs:
		kwtree.add(motif)
	# On ferme le trie, donc on peut plus ajouter de noeuds
	# Et cette fonction ajoute aussi les liens suffixes
	kwtree.finalize()
	# On cherche les motifs entrès dans le texte
	results = kwtree.search_all(text)

	finTout = time.time()

	temps = finTout - debutTout
	return results

