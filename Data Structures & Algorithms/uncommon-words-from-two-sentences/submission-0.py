class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        pass
        seen={}
        g=s1.split(" ")+s2.split(" ")
        for f in g:
            if f in seen:
                seen[f]+=1
            else:
                seen[f]=1
        l=[]
        for j,k in seen.items():
            if k<2:
                l.append(j)
        return l
            
