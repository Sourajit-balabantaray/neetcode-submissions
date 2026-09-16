class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count=0
        seen={'b':0,'a':0,'l':0,'o':0,'n':0}
        for i in text:
            if i in seen:
                seen[i]+=1
        l=[]
        l.append(seen['b'])
        l.append(seen['a'])
        l.append(seen['l']//2)
        l.append(seen['o']//2)
        l.append(seen['n'])
        return min(l)
        

        