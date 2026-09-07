class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in nums1:
            flag=0
            ind=nums2.index(i)
            for j in range(ind+1,len(nums2)):
                if i<nums2[j]:
                    l.append(nums2[j])
                    flag=1
                    break
            if flag==0:
                l.append(-1)
        return l