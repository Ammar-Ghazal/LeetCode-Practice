class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Time complexity: O(n+m), n courses, m # prerequisites
        # Space complexity: O(n+m), 
       
        indegree = [0]*numCourses # O(n) space
        adj = [[] for _ in range(numCourses)] # O(n+m) space

        # O(m) time
        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()

        # O(n) time
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        nodesVisited = 0
        while queue:
            curNode = queue.popleft()
            nodesVisited += 1

            for neighbor in adj[curNode]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                

        return nodesVisited == numCourses
