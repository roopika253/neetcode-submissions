from collections import defaultdict,deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjList = defaultdict(list)
        visited = set()
        def dfs(u,p):
            if visit[u] == 1:
                return True

            visit[u] = 1
            for c in adjList[u]:
                if c == p:
                    continue
                
                if dfs(c,u):
                    return True
            return False

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            visit = [0]*(n+1)
            if dfs(u,-1):
                return [u,v]
        return []
           
                
