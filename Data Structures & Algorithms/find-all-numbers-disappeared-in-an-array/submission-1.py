class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen=set(nums)
        l=[]
        
        for i in range(1,len(nums)+1):
            if i not in seen:
                l.append(i)
        return l
        