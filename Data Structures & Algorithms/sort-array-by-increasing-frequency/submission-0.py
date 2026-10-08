class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        seen = {}

        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1

        seen = dict(sorted(seen.items(), key=lambda x: (x[1], -x[0])))

        l = []

        for j, k in seen.items():
            l.extend([j] * k)

        return l