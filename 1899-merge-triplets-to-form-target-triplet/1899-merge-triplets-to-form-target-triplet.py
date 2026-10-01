class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        if target in triplets:
            return True
        
        last_possible = mid_possible = first_possible = 0
        for index, triplet in enumerate(triplets):
            if triplet[2] == target[2] and triplet[1] <= target[1] and triplet[0] <= target[0]:
                last_possible += 1
            if triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2]:
                mid_possible += 1
            if triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                first_possible += 1
        
        return True if (first_possible > 0 and mid_possible > 0 and last_possible > 0) else False