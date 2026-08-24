class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l1=s.split()
        return len(l1[-1])
        