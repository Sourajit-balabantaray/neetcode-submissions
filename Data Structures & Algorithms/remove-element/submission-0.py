class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        seen={val}
        num=[]
        for i in nums:
            if i not in seen:
                num.append(i)
        k=len(num)
        nums[:len(num)]=num
        nums[len(num):]=['_']*(len(nums)-len(num))
        return k
            