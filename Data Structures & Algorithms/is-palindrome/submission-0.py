class Solution:
    def isPalindrome(self, s: str) -> bool:
        i1,i2=0,len(s)-1

        while i1<i2:
            if s[i1].isalnum() and s[i2].isalnum():
                if s[i1].lower() != s[i2].lower():
                    return False
                else:
                    i1+=1
                    i2-=1
            elif s[i1].isalnum() :
                i2-=1
            
            elif s[i2].isalnum():
                i1+=1
            
            else:
                i2-=1
                i1+=1
        return True