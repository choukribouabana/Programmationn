'''
Ahocorasick implementation entirely written in python.
Supports unicode.

Quite optimized, the code may not be as beautiful as you like,
since inlining and so on was necessary

Created on Jan 5, 2016

@author: Frederik Petersen (fp@abusix.com)
'''

from builtins import object

# State représente Les noeuds du trie
class State(object):
    __slots__ = ['identifier', 'symbol', 'success', 'transitions', 'parent',
                 'matched_keyword', 'longest_strict_suffix']

    def __init__(self, identifier, symbol=None,  parent=None, success=False):
        # Le symbole du noeud
        self.symbol = symbol
        # Son identifiant (nombre entier)
        self.identifier = identifier
        # Les noeuds suivants
        self.transitions = {}
        # Le noeud père
        self.parent = parent
        # Booléen, pour savoir si le noeud correspond à un état final
        self.success = success
        # Le motif trouvé par le noeud
        self.matched_keyword = None
        # Son plus long suffixe
        self.longest_strict_suffix = None

    def __str__(self):
        transitions_as_string = ','.join(
            ['{0} -> {1}'.format(key, value.identifier) for key, value in self.transitions.items()])
        return "State {0}. Transitions: {1}".format(self.identifier, transitions_as_string)

# KeywordTree représente tout le trie
class KeywordTree(object):

    def __init__(self, case_insensitive=False):
        '''
        @param case_insensitive: If true, case will be ignored when searching.
                                 Setting this to true will have a positive
                                 impact on performance.
                                 Defaults to false.
        @param over_allocation: Determines how big initial transition arrays
                                are and how much space is allocated in addition
                                to what is essential when array needs to be
                                resized. Default value 2 seemed to be sweet
                                spot for memory as well as cpu.
        '''
        # La racine
        self._zero_state = State(0)
        # L'identifiant de la racine
        self._counter = 1
        # Booléen, qui determine si l'arbre est fermée.
        self._finalized = False
        # Determine si la recherche fait la différence entre les lettres majuscules et minuscules
        # True pour qu'il ne fasse pas la différence
        self._case_insensitive = case_insensitive

    def add(self, keyword):
        '''
        Add a keyword to the tree.
        Can only be used before finalize() has been called.
        Keyword should be str or unicode.
        '''
        if self._finalized:
            raise ValueError('KeywordTree has been finalized.' +
                             ' No more keyword additions allowed')
        # On enregistre le motif
        original_keyword = keyword
        # Si l'algorithme n'est pas sensible aux lettres
        if self._case_insensitive:
            keyword = keyword.lower()
        # Si le motif est la chaine vide
        if len(keyword) <= 0:
            return
        # On ajoute depuis l racine
        current_state = self._zero_state
        # On parcourt les caractères du motif un par un
        for char in keyword:
            try:
                # Si le symbole existe déja dans l'arbre
                # Nous suivons son chemin
                current_state = current_state.transitions[char]
            # Si le symbole n'existe pas, nous allons l'ajouter
            except KeyError:
                # On crée le noeud correspondant au symbole
                next_state = State(self._counter, parent=current_state,
                                   symbol=char)
                # On lui assigne son identifiant
                self._counter += 1
                # On crée l'état suivant
                current_state.transitions[char] = next_state
                # On passe à l'état suivant
                current_state = next_state
        # on assigne au dernier noeud du motif, l'état final.
        current_state.success = True
        current_state.matched_keyword = original_keyword




    def search_all(self, text):
        results = list()
        '''
        Search a text for all occurences of the added keywords.
        Can only be called after finalized() has been called.
        O(n) with n = len(text)
        @return: Generator used to iterate over the results.
                 Or None if no keyword was found in the text.
        '''
        if not self._finalized:
            raise ValueError('KeywordTree has not been finalized.' +
                             ' No search allowed. Call finalize() first.')
        if self._case_insensitive:
            text = text.lower()
        # On commence la recherche depuis la racine
        current_state = self._zero_state
        # on parcourt les caractères du texte un par un
        for idx, symbol in enumerate(text):
            # Depuis le noeud courant on passe au noeud suivant si le chemin existe
            # Ou on revient à la racine
            current_state = current_state.transitions.get(
                symbol, self._zero_state.transitions.get(symbol,
                                                         self._zero_state))
            # On enregistre le noeud courant
            state = current_state
            # On vérifie pour chaque noeud tous ses préfixes finaux
            while state != self._zero_state:
                if state.success:
                    keyword = state.matched_keyword
                    results.append((keyword, idx + 1 - len(keyword)))
                state = state.longest_strict_suffix
        return results

    def finalize(self):
        '''
        Needs to be called after all keywords have been added and
        before any searching is performed.
        '''
        if self._finalized:
            raise ValueError('KeywordTree has already been finalized.')
        # La racine boucle sur elle même.
        self._zero_state.longest_strict_suffix = self._zero_state
        # Nous assignons à chaque noeud son plus long suffixe
        self.search_lss_for_children(self._zero_state)
        self._finalized = True

    def search_lss_for_children(self, zero_state):
        # les noeuds qu'on a déja assigné les suffixes
        processed = set()
        # Les noeuds qui vont être traiter
        to_process = [zero_state]
        # Tant qu'il reste des noeuds sans suffixes
        while to_process:
            # On traite le premier noeud dans la liste to_process
            state = to_process.pop()
            # On ajoute son identifiant à processed
            processed.add(state.identifier)
            # On parcours les noeuds suivants le noeud actuel
            for child in state.transitions.values():
                # Si le noeud n'existe pas dans processed
                if child.identifier not in processed:
                    # On lui ajoute son lien suffixe
                    self.search_lss(child)
                    # On ajoute le noued traité à to_process
                    to_process.append(child)

    def search_lss(self, state):
        # Si le lien n'a pas été déjà attribué
        if state.longest_strict_suffix is None:
            # On enregistre le noeud parent du noeud actuel
            parent = state.parent
            # traversed pointe vers le plus long suffixe du parent
            traversed = parent.longest_strict_suffix
            while True:
                # Si le symbole sortant de noeud actuel appartient
                # au symbole sortant du noeud traversed
                # Et traversersed[symbol sortant]est différent du noeud actuel
                if state.symbol in traversed.transitions and\
                        traversed.transitions[state.symbol] != state:
                    state.longest_strict_suffix =\
                        traversed.transitions[state.symbol]
                    break
                #Sinon si traversed pointe vers la racine
                elif traversed == self._zero_state:
                    # leplus long suffixe est la racine
                    state.longest_strict_suffix = self._zero_state
                    break
                else:
                    # Sinon traversed pointe vers le plus long suffixe du traverded précedent
                    traversed = traversed.longest_strict_suffix
            # Si le plus suffixe du noeud actuel n'a pas de suffixe
            # On cherche son plus long suffixe
            suffix = state.longest_strict_suffix
            if suffix.longest_strict_suffix is None:
                self.search_lss(suffix)
            # Optimisation pour la recherche
            # On rajoute au noeud actuel un chemin vers un autre noeud
            for symbol, next_state in suffix.transitions.items():
                if (symbol not in state.transitions and
                        suffix != self._zero_state):
                    state.transitions[symbol] = next_state

    def __str__(self):
        return "ahocorapy KeywordTree"

    def __getstate__(self):
        state_list = [None] * self._counter
        todo_list = [self._zero_state]
        while todo_list:
            state = todo_list.pop()
            transitions = {key: value.identifier for key,
                           value in state.transitions.items()}
            state_list[state.identifier] = {
                'symbol': state.symbol,
                'success': state.success,
                'parent':  state.parent.identifier if state.parent is not None else None,
                'matched_keyword': state.matched_keyword,
                'longest_strict_suffix': state.longest_strict_suffix.identifier if state.longest_strict_suffix is not None else None,
                'transitions': transitions
            }
            for child in state.transitions.values():
                if len(state_list) <= child.identifier or not state_list[child.identifier]:
                    todo_list.append(child)

        return {
            'case_insensitive': self._case_insensitive,
            'finalized': self._finalized,
            'counter': self._counter,
            'states': state_list
        }

    def __setstate__(self, state):
        self._case_insensitive = state['case_insensitive']
        self._counter = state['counter']
        self._finalized = state['finalized']
        states = [None] * len(state['states'])
        for idx, serialized_state in enumerate(state['states']):
            deserialized_state = State(idx, serialized_state['symbol'])
            deserialized_state.success = serialized_state['success']
            deserialized_state.matched_keyword = serialized_state['matched_keyword']
            states[idx] = deserialized_state
        for idx, serialized_state in enumerate(state['states']):
            deserialized_state = states[idx]
            if serialized_state['longest_strict_suffix'] is not None:
                deserialized_state.longest_strict_suffix = states[
                    serialized_state['longest_strict_suffix']]
            else:
                deserialized_state.longest_strict_suffix = None
            if serialized_state['parent'] is not None:
                deserialized_state.parent = states[serialized_state['parent']]
            else:
                deserialized_state.parent = None
            deserialized_state.transitions = {
                key: states[value] for key, value in serialized_state['transitions'].items()}
        self._zero_state = states[0]
