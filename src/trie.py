class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.is_last = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertNode(self, objects, count = 1):
        current = self.root

        for o in objects:
            if o not in current.children:
                current.children[o] = TrieNode()
            current.children[o].count += count
            current = current.children[o]
            
        current.is_last = True

    def searchObject(self, objects):
        current = self.root
        found_word = []

        for o in objects:
            if o not in current.children:
                return False
            current = current.children[o]
            found_word.append((o, current.count))
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
        
