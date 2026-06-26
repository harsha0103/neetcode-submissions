from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.d=defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        value=self.d[key]
        if len(value)==0:
            return ""
        l,r=0,len(value)-1
        res=""
        while l<=r:
            mid=(l+r)//2

            if  value[mid][1]>timestamp:
                r=mid-1
            else:
                res=value[mid][0]
                l=mid+1
        return res