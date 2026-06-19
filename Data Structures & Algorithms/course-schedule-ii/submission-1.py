from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:        
        visiting= set()
        visited= set()
        course=defaultdict(list)
        for c in range(numCourses):
            course[c]
        for c,p in prerequisites:
            course[c].append(p)
        res=[]
        for c in course:
            if self.dfs(c,course,visited,visiting,res):
                return []
        return res
    
    def dfs(self,c,course,visited,visiting,res):
        if c in visited:
            return False
        
        if c in visiting:
            return True
        
        visiting.add(c)

        for pre in course[c]:
            if self.dfs(pre,course,visited,visiting,res):
                return True 
        
        visited.add(c)
        visiting.remove(c)
        res.append(c)

        return False


        