class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visiting= set()
        visited= set()
        course=defaultdict(list)
        for c in range(n):
            course[c]
        for c,p in edges:
            course[c].append(p)
            course[p].append(c)
        
        for c in course:
            if self.dfs(c,course,visited,visiting,-1):
                return False
        return True
    
    def dfs(self,c,course,visited,visiting,parent):
        if c in visited:
            return False
        
        if c in visiting:
            return True
        
        visiting.add(c)

        for pre in course[c]:
            if  pre != parent :
                if self.dfs(pre,course,visited,visiting,c):
                    return True 
        
        visited.add(c)
        visiting.remove(c)

        return False
