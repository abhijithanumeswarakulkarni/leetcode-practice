class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj_matrix = [[0] * numCourses for _ in range(numCourses)]
        inbound = {course: 0 for course in range(numCourses)}
        starts = []

        for a, b in prerequisites:
            adj_matrix[b][a] = 1
            inbound[a] += 1
        
        for course in range(numCourses):
            if inbound[course] == 0:
                starts.append(course)
        
        queue = deque(starts)
        res = []
        while queue:
            last = queue.popleft()
            res.append(last)
            for course, value in enumerate(adj_matrix[last]):
                if value == 1:
                    inbound[course] -= 1
                    if inbound[course] == 0:
                        queue.append(course)
        
        if len(res) != numCourses:
            return []
        
        return res