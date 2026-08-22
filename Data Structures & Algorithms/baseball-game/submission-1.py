class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s=[]
        for i in operations:
            if i == "+":
                if len(s)>=2:
                    p=s.pop()
                    q=s.pop()
                    r=p+q
                    s.append(q)
                    s.append(p)
                    s.append(r) 
            elif i=="D":
                t=s[-1]
                u=t*2
                s.append(u)
            elif i=="C":
                s.pop()
            else:
                s.append(int(i))
        count=0
        for j in s:
            count=count+j
        return count



        