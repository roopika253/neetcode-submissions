class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1]*n

        ans = n 


        def find(u):
            if u == par[u]:
                return  par[u]
            par[u] = find(par[u])
            return par[u]

        
        def union(u,v):
            nonlocal ans
            p1, p2 = find(u) , find(v)
            if p1 == p2:
               pass
            elif rank[p1] < rank[p2]:
                rank[p2] += rank[p1]
                par[p1] = p2
                ans -= 1
            else :
                rank[p1] += rank[p2]
                par[p2] = p1
                ans -= 1


       
        for u,v in edges:
            union(u,v)

        
        return ans 


        