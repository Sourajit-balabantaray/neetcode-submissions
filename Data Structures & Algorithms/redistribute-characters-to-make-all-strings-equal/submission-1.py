class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d={}
        s=len(words)
        for i in words:
            for j in i:
                if j in d:
                    d[j]+=1
                else:
                    d[j]=1
        for k,l in d.items():
            if d[k]<s:
                return False
            else:
                if l%s!=0:
                    return False
        return True

        