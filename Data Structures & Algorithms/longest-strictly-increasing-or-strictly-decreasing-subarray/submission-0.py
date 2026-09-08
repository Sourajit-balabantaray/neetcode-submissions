class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc=1
        dec=1
        ans=1
        i=0
        while i<len(nums)-1:
            if nums[i]>nums[i+1]:
                dec+=1
                inc=1
            elif nums[i]<nums[i+1]:
                inc+=1
                dec=1
            else:
                inc=1
                dec=1
            ans=max(inc,dec,ans)
            i+=1
        return ans

        