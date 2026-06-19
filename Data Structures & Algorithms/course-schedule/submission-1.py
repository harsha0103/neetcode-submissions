from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visiting= set()
        visited= set()
        course=defaultdict(list)
        for c in range(numCourses):
            course[c]
        for c,p in prerequisites:
            course[c].append(p)
        
        for c in course:
            if self.dfs(c,course,visited,visiting):
                return False
        return True
    
    def dfs(self,c,course,visited,visiting):
        if c in visited:
            return False
        
        if c in visiting:
            return True
        
        visiting.add(c)

        for pre in course[c]:
            if self.dfs(pre,course,visited,visiting):
                return True 
        
        visited.add(c)
        visiting.remove(c)

        return False



        