class Solution:
    def scoreOfString(self, s: str) -> int:
        count=0
        l1=list(s)
        for i in range(len(l1)-1):
            count+=abs(ord(l1[i])-ord(l1[i+1]))
        return count
        