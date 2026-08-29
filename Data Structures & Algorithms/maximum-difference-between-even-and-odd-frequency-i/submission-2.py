class Solution:
    def maxDifference(self, s: str) -> int:
        dic={}
        a1=100#float("inf")
        a2=0
        for i in s:
            dic[i]=dic.get(i,0)+1
        for i in dic.values():
            if i%2==0:
                if i<a1:
                    a1=i
            else:
                if i>a2:
                    a2=i
        diff=0
        diff=a2-a1
        return diff


        