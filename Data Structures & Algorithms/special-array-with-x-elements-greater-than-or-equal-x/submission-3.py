class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l=len(nums)
        for x in range(1,l+1):
            cnt=0
            for num in nums:
                if num>=x:
                    cnt+=1
            if cnt==x:
                return cnt
        return -1