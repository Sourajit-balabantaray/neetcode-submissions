class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l={}
        if len(s)!=len(t):
            return False
        
        for i in s:
            if i in l:
                l[i]+=1
            else:
                l[i]=1

        for i in t:
            if i in l:
                l[i]-=1
        for ctc in l.values():
             if ctc != 0:
                return False
            
        return True
       
        