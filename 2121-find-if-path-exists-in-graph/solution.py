class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # if not edges or len(edges) == 1: return False


        # Build adjacency list, note that each edge is bidirectional:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        # perform bfs:
        queue = deque([source])
        visited = set([source])

        while queue:
            cur = queue.popleft()
            if cur == destination: return True

            for neighbor in graph[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
        return False
