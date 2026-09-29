class Solution:
    def totalReplacements(self, ranks: List[int]) -> int:
        curr_top = ranks[0]
        replacements = 0

        for rank in ranks[1:]:
            if rank < curr_top:
                curr_top = rank
                replacements += 1
        
        return replacements