class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_cnt=0
        for num in nums:
            if num ==1:
                count+=1
                max_cnt=max(max_cnt,count)
            else:
                count=0
        return max_cnt