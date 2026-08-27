class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        e={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]]!=t[i]:
                    return False
            if t[i] in e:
                if e[t[i]]!=s[i]:
                    return False
            d[s[i]]=t[i]
            e[t[i]]=s[i]
        return True
