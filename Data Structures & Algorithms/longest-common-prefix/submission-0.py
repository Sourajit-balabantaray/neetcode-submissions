class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p=strs[0]
        for i in range(1,len(strs)): #acces elements from strs
            temp=""
            s = min(len(p),len(strs[i]))
            for j in range(s):
                if p[j]==strs[i][j]:
                    temp += p[j]
                else:
                    break
            p=temp
            if p=="":
                return ""
        return p





        