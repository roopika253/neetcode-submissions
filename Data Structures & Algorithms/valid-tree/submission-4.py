from collections import defaultdict,deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for i in edges:
            adjList[i[0]].append(i[1])
            adjList[i[1]].append(i[0])
        
        q = deque([(0,-1)])
        print(adjList)

        vis = set()
 
        while q:
            top = q.popleft()
            node, parent = top[0] , top[1]
            vis.add(node)
            for i in adjList[node]:
                if i == parent:
                    continue
                if i in vis:
                    return False
                q.append((i,node))
        return len(vis) == n

        