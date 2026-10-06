class Solution:
    def arraySign(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if i>0:
                l.append(1)
            elif i<0:
                l.append(-1)
            else:
                l.append(0)
        k=1
        for j in l:
            k=k*j
        return k
        