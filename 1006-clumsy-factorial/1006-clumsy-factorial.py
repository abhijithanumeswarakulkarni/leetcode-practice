class Solution:
    def clumsy(self, n: int) -> int:
        all_ops = []
        curr_op = 0
        ops_map = {
            0: '*',
            1: '/',
            2: '+',
            3: '-'
        }
        while n > 1:
            all_ops.append(n)
            all_ops.append(ops_map[curr_op])
            curr_op = (curr_op + 1) % 4
            n -= 1
        all_ops.append(1)
        
        k = len(all_ops)
        after_mul = []
        idx = 0
        while idx < k:
            item = all_ops[idx]
            if item == '*':
                var1 = after_mul.pop()
                var2 = all_ops[idx+1]
                after_mul.append(var1 * var2)
                idx += 2
            else:
                after_mul.append(item)
                idx += 1

        k = len(after_mul)
        after_div = []
        idx = 0
        while idx < k:
            item = after_mul[idx]
            if item == '/':
                var1 = after_div.pop()
                var2 = after_mul[idx+1]
                after_div.append(var1 // var2)
                idx += 2
            else:
                after_div.append(item)
                idx += 1

        k = len(after_div)
        res = after_div[0]
        idx = 1
        while idx < k:
            item = after_div[idx]
            var2 = after_div[idx+1]
            if item == '+':
                res = res + var2
            else:
                res = res - var2
            idx += 2
        
        return res