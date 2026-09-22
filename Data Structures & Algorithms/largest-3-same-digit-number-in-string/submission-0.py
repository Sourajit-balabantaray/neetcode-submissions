class Solution:
    def largestGoodInteger(self, num: str) -> str:
        seen = []
        cnt = 1

        for i in range(len(num) - 1):
            if num[i] == num[i + 1]:
                cnt += 1
            else:
                cnt = 1

            if cnt == 3:
                seen.append(num[i])

        return max(seen) * 3 if seen else ""