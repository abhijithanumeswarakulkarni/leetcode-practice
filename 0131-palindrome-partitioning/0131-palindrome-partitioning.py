class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        def solve(index, curr_str, curr_seq):
            if index == n:
                if curr_str and curr_str == curr_str[::-1]:
                    curr_seq.append(curr_str)
                if curr_seq and len("".join(curr_seq)) == n and curr_seq not in res:
                    res.append(curr_seq)
                return
            
            updated_str = curr_str + s[index]
            if updated_str == updated_str[::-1]:
                solve(index + 1, "", curr_seq + [updated_str])
            solve(index+1, updated_str, curr_seq)
        
        solve(0, "", [])
        return res