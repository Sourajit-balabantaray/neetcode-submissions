class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l1=[]
        l2=[]
        l3=[]
        l4=[]
        for i in nums:
            if i==0:
                l1.append(i)
            elif i==1:
                l2.append(i)
            else:
                l3.append(i)
        nums[:]=l1+l2+l3
        
        