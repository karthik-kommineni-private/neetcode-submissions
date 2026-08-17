class TrieNode:
       def __init__(self):
        self.children = {} # {a: trieNode1}
        self.endOfWord = False




class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:  #apple
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children.get(c)
            else:
                curr.children[c] = TrieNode()
                curr = curr.children.get(c)
        curr.endOfWord = True            

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr = curr.children.get(c)
                return False
        return curr.endOfWord         


    def startsWith(self, prefix: str) -> bool: 
        curr = self.root
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True        


        
        