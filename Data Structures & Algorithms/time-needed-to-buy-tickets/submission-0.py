class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        cnt = 0

        while tickets[k] != 0:

            l = tickets.pop(0)
            l -= 1
            cnt += 1

            if l > 0:
                tickets.append(l)

            if k == 0:
                if l == 0:
                    break
                k = len(tickets) - 1
            else:
                k -= 1

        return cnt