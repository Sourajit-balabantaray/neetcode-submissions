class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen={}
        for index,values in enumerate(nums):
            if values in seen:
                if abs(index-seen[values])<=k:
                    return True
            seen[values]=index
        return False
        