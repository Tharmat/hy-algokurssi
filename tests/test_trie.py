from src.trie import Trie
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

        self.trie.insertNode("Bugged", 10)
        self.trie.insertNode("Bug", 10)
        self.trie.insertNode([160, 66, 63])
    
    def construct_and_assert(self, input, result):
        self.assertEqual(self.trie.searchObject(input), result)
    
    def test_found1(self):
        input = "Foo"
        result = (True, [('F', 4), ('o', 4), ('o', 4)])
        self.construct_and_assert(input, result)

    def test_found2(self):
        input = "FooBar"
        result = (True, [('F', 4), ('o', 4), ('o', 4), ('B', 1), ('a', 1), ('r', 1)])
        self.construct_and_assert(input, result)

    def test_found3(self):
        input = "Whizz"
        result = (True, [('W', 1), ('h', 1), ('i', 1), ('z', 1), ('z', 1)])
        self.construct_and_assert(input, result)

    def test_not_found_1(self):
        input = "Fo"
        result = False
        self.construct_and_assert(input, result)

    def test_not_found_2(self):
        input = "Bar"
        result = False
        self.construct_and_assert(input, result)

    def test_not_found_3(self):
        input = "FoooBar"
        result = False
        self.construct_and_assert(input, result)

    def test_insert_with_count(self):
        input = "Bugged"
        result = (True, [('B', 20), ('u', 20), ('g', 20), ('g', 10), ('e', 10), ('d', 10)])
        self.construct_and_assert(input, result)

    def test_dummy_print(self):
        # For visualization
        self.trie.printNodes()

    

