class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        in_degree = {}
        adj = [[0] * (numCourses) for _ in range(numCourses)]
        
        for a, b in prerequisites:
            adj[b][a] = 1
            if a in in_degree:
                in_degree[a] += 1
            else:
                in_degree[a] = 1
                
        queue = deque()
        for course in range(numCourses):
            if course not in in_degree:
                queue.append(course)
        
        visited = [False] * numCourses
        while queue:
            course = queue.popleft()
            visited[course] = True

            for dep_course, value in enumerate(adj[course]):
                if value:
                    in_degree[dep_course] -= 1
                    
                    if in_degree[dep_course] == 0:
                        queue.append(dep_course)
        
        for visit in visited:
            if not visit:
                return False
        
        return True