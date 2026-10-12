class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        for query in queries:
            cnt = 0
            for j in range(query[0], query[1] + 1):
                if words[j][0] in "aeiou" and words[j][-1] in "aeiou":
                    cnt += 1
            result.append(cnt)

        return result
        