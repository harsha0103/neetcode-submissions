class TreeNode:
    def __init__(self):
        self.child={}
        self.word=False

class WordDictionary:

    def __init__(self):
        self.root=TreeNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.child:
                curr.child[c]=TreeNode()
            curr=curr.child[c]
        curr.word=True

        
    def search(self, word: str) -> bool:
        
        def dfs(j,root):
            curr=root

            for i in range(j,len(word)):
                if word[i] =='.':
                    for child in curr.child.values():
                        if dfs(i+1,child):
                            return True
                    return False 
                else:
                    if word[i] not in curr.child:
                        return False
                    curr=curr.child[word[i]]
            return curr.word 


        return dfs(0,self.root)