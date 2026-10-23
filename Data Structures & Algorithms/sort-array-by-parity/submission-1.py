class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=[]
        p=[]
        for i in nums:
            if i%2==0:
                l.append(i)
            else:
                p.append(i)
        return l+p
        