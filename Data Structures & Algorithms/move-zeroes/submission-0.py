class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[]
        p=[]
        for i in nums:
            if i==0:
                l.append(i)
            else:
                p.append(i)
        nums[:]=p+l
        
        