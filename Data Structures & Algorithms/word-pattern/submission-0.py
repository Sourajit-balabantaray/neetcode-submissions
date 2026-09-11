class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        seen={}
        word=s.split()
        if len(pattern)!=len(word):
            return False
        else:
            for i in range(len(word)):
                if pattern[i] in seen:
                    if seen[pattern[i]]!=word[i]:
                        return False
                else:
                    if word[i] in seen.values():
                        return False
                    seen[pattern[i]]=word[i]
        return True