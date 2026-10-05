class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_matrix = [[0] * numCourses for _ in range(numCourses)]
        inbound = {}
        starts = []
        
        for a, b in prerequisites:
            adj_matrix[b][a] = 1
            if a in inbound:
                inbound[a] += 1
            else:
                inbound[a] = 1
        
        for course in range(numCourses):
            if course not in inbound:
                starts.append(course)
        
        if len(inbound) == 0:
            return True

        if len(starts) == 0:
            return False
        
        visited = [False] * numCourses
        for start in starts:
            queue = [start]

            while queue:
                last = queue.pop(0)
                visited[last] = True
                for course, value in enumerate(adj_matrix[last]):
                    if value == 1 and not visited[course]:
                        inbound[course] -= 1
                        if inbound[course] == 0:
                            queue.append(course)
            
        res = visited[0]
        
        for visit in visited[1:]:
            res = res and visit
        
        return res