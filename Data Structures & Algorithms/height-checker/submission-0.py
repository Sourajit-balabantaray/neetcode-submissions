class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l=heights.copy()
        l.sort()
        cnt=0
        for i in range(len(heights)):
            if heights[i]!=l[i]:
                cnt+=1
        return cnt
        