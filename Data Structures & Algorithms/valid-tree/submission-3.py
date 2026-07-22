from collections import defaultdict
from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adjList = defaultdict(list)
        for i in edges:
           adjList[i[0]].append(i[1])
           adjList[i[1]].append(i[0])
           
        visited = set()
        queue = deque()
        queue.append([0,-1])
        visited.add(0)
        while queue:
            child , parent = queue.popleft()
            for i in adjList[child]:
                if i == parent:
                    continue
                if i in visited:
                    return False
                queue.append([i,child])
                visited.add(i)
        return len(visited) == n




        