from src.trie import Trie
from src.markov import Markov
import unittest

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.insertNode("Foo")
        self.trie.insertNode("Foo")
        self.trie.insertNode("Fooo")
        self.trie.insertNode("FooBar")
        self.trie.insertNode("foo")
        self.trie.insertNode("Whizz")

    def test_dummy(self):
        markov = Markov()
        markov.run(self.trie)