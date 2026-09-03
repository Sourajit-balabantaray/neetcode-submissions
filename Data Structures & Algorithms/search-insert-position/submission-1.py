class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)
        mid=0
        found=0
        while low<high:
            mid=(low+high)//2
            if nums[mid]==target:
                found=1
                return mid
            elif nums[mid]>target:
                high=mid
            elif nums[mid]<target:
                low=mid+1
        return low
            
        
        