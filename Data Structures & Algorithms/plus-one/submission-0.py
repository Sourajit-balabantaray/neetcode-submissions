class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j=1
        s=len(digits)
        sum=0
        for i in digits:
            if j<=len(digits):
                l=i*(10**(s-j))
                sum=sum+l
                j+=1
            else:
                break
        sum+=1
        d=sum
        k=[]
        while d!=0:
            d1=d%10
            k.append(d1)
            d=d//10
        k.reverse()
        return k

        