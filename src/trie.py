class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.is_last = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertWord(self, word):
        current = self.root

        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current.children[letter].count += 1
            current = current.children[letter]
            
        current.is_last = True

    def searchWord(self, word):
        current = self.root

        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.is_last
    
def printNodes(node, depth = 0):
    for key, value in node.children.items():
        print(" " * depth, end = " ")
        print(key, ":", value.count)
        depth += 1
        printNodes(node.children[key], depth)
        depth -= 1
        
