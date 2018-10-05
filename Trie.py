from collections import defaultdict
import re

class TrieNode(object):
    def __init__(self):
        """Node object.
        Next is child.
        Nodes are connected via defaultdicts.
        End of word is marked by leaf node.
        Leaf node is true or false."""
        # Nodes are connected via defaultdicts
        self.next = defaultdict(TrieNode)
        self.isleaf = False
        
    def __str__(self):
        """Print function: prints a visual representation of the trie.
        Leaf node marked by $."""
        s = ""
        if self.isleaf:
            s = "$, "
        for key, value in self.next.items():
            s = s + key + "(" + value.__str__() + "), "
        return s[0:-2]

class Trie(object):
    def __init__(self):
        """Initialize the object as root."""
        self.root = TrieNode()
        
    def __str__(self):
        """Print visual representation of trie if trie not empty."""
        if self.root:
            return self.root.__str__()
        else:
            return "Empty tree"
    
    def insert(self, word):
        """Insert word in trie.
        Filter out words longer than 35 chars.
        Input is a word."""
        if not word:
            return
        # Change this value if you want to allow longer or shorter words
        if len(word) < 35:
            node = self.root
            for char in word:
                node = node.next[char]
            node.isleaf = True
        else:
            raise Exception("Word too long " + str(len(word)) + " chars")
        
    def search(self, word):
        """Perform an exact search.
        Input is a word.
        Output is boolean."""
        if not word or word == "":
            return False
        node = self.root
        for char in word:
            if char in node.next:
                node = node.next[char]
            else:
                return False
        return node.isleaf
    
    def startswith(self, prefix):
        """Perform a prefix search.
        Input is a prefix.
        Output is boolean."""
        node = self.root
        i = 0
        for char in prefix:
            if char in node.next:
                node = node.next[char]
            else:
                return False
            i += 1
        return True if i == len(prefix) else False
