class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=[]
        s=[]
        for i in operations:
            if i == "+":
                if len(l)>=2:
                    p=l.pop()
                    q=l.pop()
                    r=p+q
                    s.append(r)
                    l.append(q)
                    l.append(p)
                    l.append(r)
            elif i=="D":
                t=l[-1]
                u=t*2
                s.append(u)
                l.append(u)
            elif i=="C":
                s.pop()
                l.pop()
            else:
                s.append(int(i))
                l.append(int(i))
        count=0
        for j in s:
            count=count+j
        return count



        