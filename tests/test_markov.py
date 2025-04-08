from src.trie import Trie
from src.markov import Markov
import unittest

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.insertWord("Foo")
        self.trie.insertWord("Foo")
        self.trie.insertWord("Fooo")
        self.trie.insertWord("FooBar")
        self.trie.insertWord("foo")
        self.trie.insertWord("Whizz")

    def test_dummy(self):
        markov = Markov()
        markov.run(10, self.trie)