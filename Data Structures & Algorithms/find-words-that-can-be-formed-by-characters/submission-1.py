class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        seen = {}

        for i in chars:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1

        sums = 0

        for word in words:
            count = {}

            for ch in word:
                if ch in count:
                    count[ch] += 1
                else:
                    count[ch] = 1

            flag = 0

            for ch in count:
                if ch not in seen or count[ch] > seen[ch]:
                    flag = 1
                    break

            if flag == 0:
                sums += len(word)

        return sums