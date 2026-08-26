class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        seen=set()
        for i in words:
            for j in words:
                if i != j and j in i:
                    seen.add(j)
                
        return list(seen)

        
        