class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        s={}
        l=[]
        for i in arr1:
                s[i]=s.get(i,0)+1
        for j in arr2:
            l.extend([j]*s[j])
            del s[j]
        for j in sorted(s):
            l.extend([j]*s[j])
        return l
