"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        # dict to save {visited node: its respective clone}
        self.visited = {}
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Time complexity: O(n+m), n is # of nodes and m is # of edges
        # Space cmplexity: O(n)
        if not node: return node

        if node in self.visited:
            return self.visited[node]
        
        clone = Node(node.val, [])

        self.visited[node] = clone

        for neighbor in node.neighbors:
            clone.neighbors.append(self.cloneGraph(neighbor))

        return clone





        # # ----- BFS IMPLEMENTATION -----------------------
        # # Time complexity: O(n+m), n is # of nodes and m is # of edges
        # # Space complexity: O(n), for visited dict
        # # Dictionary: {visited node: clone of that node}
        # visited = {}

        # # create the bfs queue and store first node into visited
        # queue = deque([node])
        # visited[node] = Node(node.val, [])

        # while queue:
        #     cur = queue.popleft()
        #     for neighbor in cur.neighbors:
        #         if neighbor not in visited:
        #             visited[neighbor] = Node(neighbor.val, [])
        #             queue.append(neighbor)
        #         # add each cloned neighbor of cur into the clone's neighbors
        #         visited[cur].neighbors.append(visited[neighbor])
        
        # return visited[node]
