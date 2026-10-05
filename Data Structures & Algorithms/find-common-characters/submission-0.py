class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        d = []
        k = words[0]

        for i in range(len(k)):
            flag = 0

            for j in range(len(words)):
                if k[i] not in words[j]:
                    flag = 1
                    break

            if flag == 0:
                d.append(k[i])

                for j in range(len(words)):
                    words[j] = words[j].replace(k[i], "", 1)

        return d