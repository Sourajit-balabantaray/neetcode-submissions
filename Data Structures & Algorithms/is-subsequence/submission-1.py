class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
             l=t.find(i)  
             if l==-1:
                return False
             t=t[l+1:]

        return True
        