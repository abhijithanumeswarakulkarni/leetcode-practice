class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        res = []
        people.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        queue = deque(people)

        while queue:
            height, count = queue.popleft()
            curr_count = 0
            idx = 0
            n = len(res)
            while idx < n and curr_count != count:
                item = res[idx]
                if item[0] >= height:
                    curr_count += 1
                idx += 1
            if curr_count == count:
                res.insert(idx, [height, count])
            else:
                queue.append([height, count])
        
        return res