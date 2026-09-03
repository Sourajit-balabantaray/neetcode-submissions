class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        mid=0
        found=0
        while low<high:
            mid=(low+high)//2
            if nums[mid]==target:
                found=1
                return mid
            elif nums[mid]>target:
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
        i=0
        if found==0:
            while i<len(nums) and nums[i]<target:
                i+=1
        return i
            
        
        