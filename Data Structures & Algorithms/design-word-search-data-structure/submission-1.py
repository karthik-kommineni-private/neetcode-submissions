class TreeNode:
    def __init__(self):
        self.children = defaultdict(TreeNode)
        self.end = False




class WordDictionary:

    def __init__(self):
        self.root = TreeNode()     

    def addWord(self, word: str) -> None: #apple
        curr = self.root
        for c in word: 
            curr= curr.children[c]
        curr.end = True    
        
    def search(self, word: str) -> bool:
        return self.helper(self.root, word)


    def helper(self, curr_node, word):
        for i, c in enumerate(word):  #.ay #a..
            if c == ".":
                for child in curr_node.children.values(): #explore all children
                    if self.helper(child, word[i+1:]):
                        return True
                return False    
            if c not in curr_node.children:
                return False
            curr_node = curr_node.children[c]
        return curr_node.end



        
