class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        seen={}
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        for j in seen.values():
            if j%2!=0:
                return False
        return True

        