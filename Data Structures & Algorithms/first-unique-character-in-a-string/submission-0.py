class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen={}
        for i in s:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        
        for j in range(len(s)):
            if seen[s[j]]==1:
                return j
        return -1
        