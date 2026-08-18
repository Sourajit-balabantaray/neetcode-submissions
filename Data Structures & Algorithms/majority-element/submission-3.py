class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
            if count[i]>len(nums)/2:
                return i
        