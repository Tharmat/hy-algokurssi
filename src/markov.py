import random
from trie import Trie

class Markov:

    # TODO: POC version of nth order markov chain. Currently for only 2nd order Markov
    # Assumes that the Trie data structure depth is correct for the given order (order + 1)
    # Currently chooses the required to "start" elements for 2nd order Markov chain by walking
    # through the trie using given probabilities
    def run(self, trie: Trie, order=2, iterations=16):
        start = self.pick_n(trie, order)
        print("Picking start:", start)
        print("---------")

        notes = []

        for i in range(iterations):
            current = trie.root

            # For debugging
            print("Iteration:", i, "start:", start)
            for x in range(order + 1):
                children = current.children

                # Walk through the trie structure if depth is < order
                if x < (order):

                    # Sanity check
                    if start[x] not in children:
                        print("Start", start[x], "not found in Trie at position", x)
                        return False
                    current = children[start[x]]
                    continue

                # When x = order + 1 pick the next note based on the current children.
                # Population is the children of the node that we've arrived using the start values (a, b) -> c
                population = list(children.keys())

                # Weights are the given values for each child (key). These are the number of times the specific note is seen in
                # this context when ingesting midi file
                weights = [node.count for node in children.values()]

                # Sanity check
                assert len(population) == len(weights)

                # For debugging
                print("Population:", population, "Weights:", weights)

                # Choose the next note using choices which takes a population list and equal sized list of weight
                next_note = random.choices(population=population, weights=weights)[0]

                # For debugging
                print("Next:", next_note)

                # Append the note to the list of generated notes
                notes.append(next_note)
            
            # Update the start two notes for next iteration
            start = [start[1], notes[-1]]

        print("Markov chain finished with results:", notes)
        print("---------")
        return notes

    def pick_n(self, trie: Trie, n):
        current = trie.root
        notes = []

        for _ in range(n):
            children = current.children

            # Pick the next state based on the probabilities
            population = list(children.keys())
            weights = [node.count for node in children.values()]

            # Sanity check
            assert len(population) == len(weights)

            # Choose the next state
            next_note = random.choices(population=population, weights=weights)[0]
            notes.append(next_note)
            current = children[next_note]
        
        # Sanity check
        assert(len(notes) == n)
        return notes