class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for i in details:
            l=i[11:13]
            if int(l)>60:
                count+=1
        return count

        