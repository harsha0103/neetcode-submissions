class CountSquares:

    def __init__(self):
        self.point=defaultdict(int)
        self.arr=[]

    def add(self, point: List[int]) -> None:
        self.point[tuple(point)]+=1
        self.arr.append(tuple(point))
    def count(self, point: List[int]) -> int:
        res=0
        px,py=point

        for x,y in self.arr:
            if (abs(px-x)==abs(py-y)) and x!=px and y!=py:
                res+=self.point[(x,py)] * self.point[(y,px)]

            
            else:
                continue
                
        return res
