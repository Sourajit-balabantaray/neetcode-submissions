class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l=[]
        for i in arr2:
            for j in arr1:
                if j==i:
                    l.append(j)
        s=[]
        for k in arr1:
            if k not in l:
                s.append(k)
        s.sort()
        return l+s
        