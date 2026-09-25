class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen=set()
        q=len(nums)
        
        for i in range(q):
            if nums[i] in seen:
                dup=nums[i]
            seen.add(nums[i])
        for j in range(1,q+1):
            if j not in seen:
                miss=j
        
        return [dup,miss]
            