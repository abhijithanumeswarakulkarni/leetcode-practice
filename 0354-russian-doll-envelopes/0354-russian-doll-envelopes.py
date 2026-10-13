class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # # DP Soln - TLE
        # envelopes.sort()
        # n = len(envelopes)
        # nxt = [0] * (n + 1)

        # for index in range(n-1, -1, -1):
        #     curr = [-1] * (n + 1)
        #     for prev in range(index + 1, n+1):
        #         fit = 0
        #         if prev == n or envelopes[index][0] > envelopes[prev][0] and envelopes[index][1] > envelopes[prev][1]:
        #             fit = 1 + nxt[index]
        #         not_fit = nxt[prev]
        #         curr[prev] = max(fit, not_fit)
        #     nxt = curr
        
        # return nxt[n]

        envelopes.sort(key= lambda item: (item[0], -item[1]))
        heights = list(map(lambda x: x[1], envelopes))
        tails = []
        for x in heights:
            i = bisect_left(tails, x)
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)