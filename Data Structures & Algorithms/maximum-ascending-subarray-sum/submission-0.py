class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        l = []
        s = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                s.append(nums[i])
            else:
                l.append(s)
                s = [nums[i]]

        l.append(s)

        k = []

        for j in l:
            k.append(sum(j))

        return max(k)