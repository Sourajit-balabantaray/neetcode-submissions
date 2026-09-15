class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen=set()
        l=[]
        count=0
        for i in grid:
            for j in i:
                if j in seen:
                    l.append(j)
                else:
                    seen.add(j)
                count+=1
        q=list(seen)
        for k in range(1,count+1):
            if k not in q:
                l.append(k)
        return l