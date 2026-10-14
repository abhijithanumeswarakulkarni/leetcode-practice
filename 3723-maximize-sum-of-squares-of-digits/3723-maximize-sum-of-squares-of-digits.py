class Solution:
    def maxSumOfSquares(self, num: int, add: int) -> str:
        # # Bruteforce - TLE
        # def sumOfSquares(curr_num):
        #     sum_squares = 0
        #     for digit in curr_num:
        #         sum_squares += int(digit) ** 2
        #     return sum_squares
        
        # def solve(curr_num, k, prev_sum):
        #     if prev_sum > add:
        #         return ""

        #     if k == 0:
        #         return curr_num if prev_sum == add else ""
            
        #     res = ""
        #     maxi = float('-inf')
        #     for digit in range(10):
        #         if digit == 0 and not curr_num:
        #             continue
        #         ans = solve(curr_num + str(digit), k - 1, prev_sum + digit)
        #         sum_squares = sumOfSquares(ans)
        #         if sum_squares >= maxi and (not res or (res and ans and int(ans) > int(res))):
        #             res = ans
        #             maxi = sum_squares
        #     return res
        
        # return solve("", num, 0)

        # Greedy
        curr_score = 0
        res = ""
        while num > 0:
            for digit in range(9, -1, -1):
                if digit <= add:
                    curr_score += digit ** 2
                    add -= digit
                    res += str(digit)
                    break
            num -= 1
        return res if add == 0 else ""