class Solution:
    def reverseWords(self, s: str) -> str:
        pass
        k=s.split(" ")
        l=[]
        for i in k:
            i=i[::-1]
            l.append(i)
        p=""
        for j in l:
            p=p+j+" "
        return p.rstrip()
