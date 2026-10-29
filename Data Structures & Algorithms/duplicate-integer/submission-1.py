class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for values in nums:
            if values in seen:
                return True
            seen.add(values)
        return False        