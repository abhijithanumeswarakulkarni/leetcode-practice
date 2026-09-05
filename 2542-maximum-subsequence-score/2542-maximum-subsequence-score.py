class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # n = len(nums1)
        # def solve(index, k, currMin, currSum, dp):
        #     if k == 0:
        #         return currMin * currSum

        #     if index == n:
        #         return float('-inf')
            
        #     if (index, k, currMin, currSum) not in dp:
        #         opt1 = solve(index+1, k-1, min(currMin, nums2[index]), currSum + nums1[index], dp)
        #         opt2 = solve(index+1, k, currMin, currSum, dp)

        #         dp[(index, k, currMin, currSum)] = max(opt1, opt2)
        #     return dp[(index, k, currMin, currSum)]
        
        # dp = {}
        # return solve(0, k, float('inf'), 0, dp)

        pairs = []
        n = len(nums1)
        for idx in range(n):
            pairs.append((nums1[idx], nums2[idx]))
        
        pairs = list(sorted(pairs, key= lambda x: -x[1]))
        maxi = float('-inf')
        heap = []
        currSum = 0
        for i in range(n):
            heapq.heappush(heap, pairs[i][0])
            currSum += pairs[i][0]
            if len(heap) > k:
                currSum -= heapq.heappop(heap)
            if len(heap) == k:
                maxi = max(maxi, currSum * pairs[i][1])
        
        return maxi