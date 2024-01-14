class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        # go through each char
        for char in word:
            # create new child
            if char not in node.children:
                node.children[char] = TrieNode()
            # move to child
            node = node.children[char]
        # node for a completed word
        node.is_word = True
        
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        # go through each char
        for char in word:
            # no this char
            if char not in node.children:
                return False
            # move to child
            node = node.children[char]
        # check if it is a word
        return node.is_word
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        # go through each char
        for char in prefix:
            # no this char
            if char not in node.children:
                return False
            # move to child
            node = node.children[char]
        return True


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
