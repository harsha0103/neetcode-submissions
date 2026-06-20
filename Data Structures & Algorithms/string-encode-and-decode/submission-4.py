class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=s+"@#@"
        return res

    def decode(self, s: str) -> List[str]:
        arr=s.split("@#@")
        arr.pop()
        return arr