from src.trie import Trie, TrieNode, printNodes
import unittest

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.debug = True
        self.trie.insertWord("Foo")
        self.trie.insertWord("Foo")
        self.trie.insertWord("Fooo")
        self.trie.insertWord("FooBar")
        self.trie.insertWord("foo")
        self.trie.insertWord("Whizz")

    def test_found(self):
        printNodes(self.trie.root)
        self.assertEqual(self.trie.searchWord("Foo"), True)
        self.assertEqual(self.trie.searchWord("FooBar"), True)
        self.assertEqual(self.trie.searchWord("Whizz"), True)
        
    def test_not_found(self):
        self.assertEqual(self.trie.searchWord("Fo"), False)
        self.assertEqual(self.trie.searchWord("Bar"), False)
        self.assertEqual(self.trie.searchWord("FoooBar"), False)
