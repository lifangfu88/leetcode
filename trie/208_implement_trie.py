class Node:
    def __init__(self, val):
        # true if the node is end of word
        self.is_word = False
        # max length 26
        self.next = {}
        # current character value
        self.val = val


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        init dummy root node
        """
        self.root = Node(0)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        if not word or not word.isalpha():
            return

        node = self.root
        for c in word:
            # create new node only when it's a new char
            if c not in node.next:
                node.next[c] = Node(c)
            node = node.next[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node.next:
                return False
            node = node.next[c]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        if self.search(prefix):
            return True

        node = self.root
        for c in prefix:
            if c not in node.next:
                return False
            node = node.next[c]
        # all the char in prefix exist in a branch, there must be a word
        return True

    def dfs(self, node):
        """
        dfs to search if any child node is a word
        :param node:
        :return:
        """
        if not node:
            return False
        if node.is_word:
            return True

        for node in node.next.values():
            return self.dfs(node)


if __name__ == '__main__':
    trie = Trie()
    trie.insert('apps')
    trie.insert('apple')
    print(trie.search('apps'))


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
