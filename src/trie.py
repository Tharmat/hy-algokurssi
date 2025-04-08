class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.is_last = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertWord(self, word, count = 1):
        current = self.root

        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current.children[letter].count += count
            current = current.children[letter]
            
        current.is_last = True

    def searchWord(self, word):
        current = self.root
        found_word = []

        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
            found_word.append((letter, current.count))
        if current.is_last:
            return True, found_word
        return False
    
    def printNodes(self, node = None, depth = 0):
        if node is None:
            print()
            node = self.root
        for key, value in node.children.items():
            print(" " * depth, end = " ")
            print(key, ":", value.count)
            depth += 1
            self.printNodes(node.children[key], depth)
            depth -= 1
        
