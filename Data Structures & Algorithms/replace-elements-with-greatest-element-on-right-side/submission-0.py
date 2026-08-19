class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxele=-1
        for i in range(len(arr)-1,-1,-1):
            current=arr[i]
            arr[i]=maxele
            maxele=max(maxele,current)
            
        return arr
        