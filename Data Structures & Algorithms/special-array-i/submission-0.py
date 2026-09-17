class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        def even(k):
            if k%2==0:
                return True
            else:
                return False
        if len(nums)==1:
            return True
        for i in range(len(nums)):
            if even(i)==True:
                if even(nums[i])==False:
                    return False
            else:
                if even(nums[i])==True:
                    return False
        return True
