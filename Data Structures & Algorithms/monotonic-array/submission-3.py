class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0]>nums[1]:
            for i in range(len(nums)-1):
                if (nums[i]>=nums[i+1])==False:
                    return False
        elif nums[0]<nums[1]:
            for j in range(len(nums)-1):
                if (nums[j]<=nums[j+1])==False:
                    return False
        else:
            cnt=0
            for k in range(len(nums)-1):
                if nums[k]==nums[k+1]:
                    cnt+=1
                else:
                    break
            if cnt==len(nums)-1:
                return True
            elif nums[cnt]>nums[cnt+1]:
                for i in range(len(nums)-1):
                    if (nums[i]>=nums[i+1])==False:
                        return False
            elif nums[cnt]<nums[cnt+1]:
                for j in range(len(nums)-1):
                    if (nums[j]<=nums[j+1])==False:
                         return False
            
        return True
        