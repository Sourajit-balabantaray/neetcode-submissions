class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        mid=0
        while mid<=end:
            left=0
            right=0
            for i in range(start,mid):
                left+=nums[i]
            for j in range(mid+1,end+1):
                right+=nums[j]
            if left==right:
                return mid
            mid+=1
        return -1
            
            