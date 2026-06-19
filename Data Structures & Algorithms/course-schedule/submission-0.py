from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited=set()
        visiting=set()
        res=[]
        graph={}
        for i in range(numCourses):
            graph[i]=[]
        for course,pre in prerequisites:
            graph[course].append(pre)

        for course in graph:
            if self.dfs_traverse(graph,course,visiting,visited,res):
                return False
        print(res)
        return True 
    
    def dfs_traverse(self,graph,course,visiting,visited,res):
        if course in visiting:
            return True
        
        if course in visited:
            return False
        visiting.add(course)
        for pre in graph[course]:
            if self.dfs_traverse(graph,pre,visiting,visited,res):
                return True
        
        visited.add(course)
        visiting.remove(course)
        res.append(course)
        return False

        


        