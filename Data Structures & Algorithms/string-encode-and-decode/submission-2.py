class Solution:

    def encode(self, strs: List[str]) -> str:
        s=[]
        for i in strs:
            s.append(str(len(i))+"#"+i)
        return " ".join(s)


    def decode(self, s: str) -> List[str]:
        start = 0
        l1 = []

        while start < len(s):
            hasidx = s.find("#", start)
            length = int(s[start:hasidx])

            start = hasidx + 1
            word = s[start:start + length]

            l1.append(word)
            start = start + length

        return l1
            

        
            
