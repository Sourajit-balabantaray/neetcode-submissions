class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        l=customers[0][0]
        p=[]
        for i in customers:
            l=max(l,i[0])
            l+=i[1]
            p.append(l-i[0])
        avg=sum(p)/len(p)
        return avg

        