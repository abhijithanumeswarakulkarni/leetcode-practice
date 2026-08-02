class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket1 = {}
        basket2 = {}
        l, r = 0, 0
        n = len(fruits)
        res = 0

        while r < n:
            curr_fruit = fruits[r]
            if curr_fruit in basket1:
                basket1[curr_fruit] += 1
            elif curr_fruit in basket2:
                basket2[curr_fruit] += 1
            elif not basket1:
                basket1[curr_fruit] = 1
            elif not basket2:
                basket2[curr_fruit] = 1
            else:
                while (l < r):
                    if fruits[l] in basket1:
                        if basket1[fruits[l]] > 1:
                            basket1[fruits[l]] -= 1
                        else:
                            del basket1[fruits[l]]
                            basket1[curr_fruit] = 1
                            break
                    else:
                        if basket2[fruits[l]] > 1:
                            basket2[fruits[l]] -= 1
                        else:
                            del basket2[fruits[l]]
                            basket2[curr_fruit] = 1
                            break
                    l += 1
                l += 1
            res = max(res, (r-l+1))
            r += 1
            
        return res