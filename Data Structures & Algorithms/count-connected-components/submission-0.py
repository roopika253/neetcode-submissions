from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        vis = [0]*n

        ans = 0

        def dfs(i , adjList, vis):
            if vis[i] == 1:
                return 
            vis[i] = 1
            for j in adjList[i]:
               dfs(j, adjList , vis)
       

        for i in range(n):
            if vis[i] != 1:
                ans += 1
                dfs(i, adjList , vis)
        
        return ans
            
        

        