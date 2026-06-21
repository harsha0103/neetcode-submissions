class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i1,i2=0,len(numbers)-1
        while i1<i2:
            s1=numbers[i1]+numbers[i2]

            if s1>target:
                i2-=1
            elif s1<target:
                i1+=1
            else:
                return [numbers[i1],numbers[i2]]
        return []