class Solution:
    def findLucky(self, arr: List[int]) -> int:
        seen={}
        for i in arr:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        l=[]
        for f,g in seen.items():
            if int(f)==g:
                l.append(g)
        if l!=[]:
            return max(l)
        else:
            return -1        