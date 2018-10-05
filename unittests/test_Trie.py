import sys
sys.path.append('../')

import Trie
import unittest
import uuid 
import random
import string
import secrets
import timeit

def list_complexity(list, words):
    """Estimate complexity of lookup with a list.""" 
    start_time = timeit.default_timer()
    for word in words:
        if word in list:
            continue
    return timeit.default_timer() - start_time

def tree_complexity(tree, words):
    """Estimate complexity of lookup with trie."""
    start_time = timeit.default_timer()
    for word in words:
        tree.search(word)
    return timeit.default_timer() - start_time

def create_test_set(n):
    """Create a test set of random strings.
    Input size of lexicon.
    Output list of words."""
    test_set = []
    for i in range(n):
        random_word = ''.join(secrets.choice(string.ascii_lowercase) for i in range(5))
        test_set.append(random_word)
    return test_set

def build(tree, list, n):
    """Build a trie.
    Input trie, """
    for i in range(n):
        random_word = ''.join(secrets.choice(string.ascii_lowercase) for j in range(5))
        tree.insert(random_word)
        list.append(random_word)
    return tree, list


def test_insertion():
    """Test behavior of trie."""
    tree = Trie.Trie()
    words = ["monkey", "monkeybusiness", "banana", "monkey", "bananas", "bananas", "m"]

    for word in words:
        tree.insert(word)
    return tree


class TestInsert(unittest.TestCase):
    def test_complexity(self):
        empty_tree = Trie.Trie()
        empty_list = []
        test_set = create_test_set(100)
        tree, list = build(empty_tree, empty_list, 100000)
        tree_time = tree_complexity(tree, test_set)
        list_time = list_complexity(list, test_set)
        self.assertTrue(list_time>tree_time)
    
    def test_behaviour(self):
        trie = test_insertion()
        self.assertTrue(trie.search("monkey"))
        self.assertTrue(trie.search("monkeybusiness"))
        self.assertTrue(trie.search("banana"))
        self.assertTrue(trie.search("bananas"))
        self.assertTrue(trie.search("b")==False)
        self.assertTrue(trie.search("")==False)
        self.assertTrue(trie.search("orange")==False)
        self.assertTrue(trie.search("monk")==False)

if __name__ == '__main__':
    unittest.main()
