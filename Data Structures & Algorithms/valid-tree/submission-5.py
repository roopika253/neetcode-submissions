from collections import defaultdict
class Solution:

    def dfs(self, node, parent, vis, adjList):
        vis[node] = 1
        for i in adjList[node]:
            if i == parent:
                continue
            if vis[i] == 1:
                return False
            if not self.dfs(i, node, vis, adjList):
                return False
        return True
         
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        vis = [0]*n
        for i in range(len(edges)):
            adjList[edges[i][0]].append(edges[i][1])
            adjList[edges[i][1]].append(edges[i][0])
        
        if not self.dfs(0, -1, vis, adjList):
            return False
        return sum(vis) == n
      
        