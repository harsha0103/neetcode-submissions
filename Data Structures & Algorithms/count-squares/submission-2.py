from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.arr=[]
        self.cou=defaultdict(int)


    def add(self, point: List[int]) -> None:
        self.arr.append(tuple(point))
        self.cou[tuple(point)]+=1


    def count(self, point: List[int]) -> int:
        res=0
        px,py=point

        for x,y in self.arr:
            if (abs(x-px)==abs(y-py)) and x!=px and y!=py:
                res+=self.cou[(x,py)]*self.cou[(px,y)]
            else: continue
    
        return res

