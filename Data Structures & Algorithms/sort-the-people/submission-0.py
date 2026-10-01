class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dec={}
        for i in range(len(names)):
            dec[heights[i]]=names[i]
        heights.sort(reverse=True)
        l=[]
        for j in heights:
            l.append(dec[j])
        return l
