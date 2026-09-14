class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        s={}
        for i in arr:
           s[i]= s.get(i,0)+1
        l=[]
        for j in s:
            if s[j]==1:
                l.append(j)
        if l==[]:
            return ""
        elif k<=len(l):
            return l[k-1]
        return ""