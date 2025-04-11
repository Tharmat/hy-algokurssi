from src.trie import Trie
import random

class Markov:

    # Simple first order Markov chain
    def run(self, transitions, trie: Trie):

        for _ in range(transitions):
            current = trie.root
            children = current.children

            word = []

            while current.children:
                children = current.children

                # If at the end of chain, return False even if there were transitions left
                if not children:
                    break
                
                # Pick the next state based on the probabilities
                population = list(children.keys())
                weights = [node.count for node in children.values()]

                # Sanity check
                assert(len(population) == len(weights))

                # For debug
                print("Population:", population, "Weights:", weights)

                # Choose the next state
                next = random.choices(population = population, weights = weights)[0]
                
                # For debug
                word.append(next)
                current = children[next]
            
            print(word)

