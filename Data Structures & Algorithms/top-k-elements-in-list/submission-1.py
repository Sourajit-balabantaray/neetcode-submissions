class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l={}
        for i in nums:
            l[i]=l.get(i,0)+1
        l2=[]
        l3=[]
        for i in l:
            l2.append(i)
        l2.sort(key=lambda i: l[i],reverse=True)
        l3=l2[:k]
        return l3