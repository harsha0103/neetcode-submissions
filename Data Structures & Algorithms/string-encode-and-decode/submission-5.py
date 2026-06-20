class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        i=0
        arr=[]
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            num=int(s[i:j])
            j+=1
            new_str=s[j:j+num]
            arr.append(new_str)
            i=j+num
        return arr