class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        res = []
        friends = set(friends)
        
        for o in order:
            if o in friends:
                res.append(o)
        
        return res