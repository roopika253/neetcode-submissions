class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for i in prerequisites:
            adjList[i[1]].append(i[0])

        indegree = [0]*numCourses

        for i in adjList:
            for j in adjList[i]:
                indegree[j] += 1

        q = deque()
        topo = []

        for i,ind in enumerate(indegree):
            if ind == 0:
                q.append(i)
        
        while q:
            top = q[0]
            q.popleft()
            topo.append(top)
            for i in adjList[top]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        
        if len(topo) == numCourses :
            return topo
        else :
            return []
        