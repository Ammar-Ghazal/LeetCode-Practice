class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        import heapq
        
        # Two graphs: one with cost (forward), one with cost*tax (return with apples)
        fwd_graph = [[] for _ in range(n)]
        ret_graph = [[] for _ in range(n)]
        for u, v, cost, tax in roads:
            fwd_graph[u].append((v, cost))
            fwd_graph[v].append((u, cost))
            ret_graph[u].append((v, cost * tax))
            ret_graph[v].append((u, cost * tax))
        
        def dijkstra(src, graph):
            dist = [float('inf')] * n
            dist[src] = 0
            heap = [(0, src)]
            while heap:
                d, u = heapq.heappop(heap)
                if d > dist[u]:
                    continue
                for v, w in graph[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(heap, (nd, v))
            return dist
        
        ans = [0] * n
        for i in range(n):
            fwd = dijkstra(i, fwd_graph)
            ret = dijkstra(i, ret_graph)
            best = prices[i]
            for j in range(n):
                total = prices[j] + fwd[j] + ret[j]
                if total < best:
                    best = total
            ans[i] = best
        
        return ans
