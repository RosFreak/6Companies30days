# problem Link
# https://leetcode.com/problems/course-schedule/description/

class Solution:
    def buildAdjacency(self,n,edges):
        adjList = [[] for _ in range(n)]
        for c1, c2 in edges:
            adjList[c2].append(c1)
        return adjList
    def topoSort(self , n , edges):
        adjList = self.buildAdjacency(n , edges)
        inDegrees = [0] * n
        for v1, v2 in edges:
            inDegrees[v1] += 1
        queue = []
        for v in range(n):
            if inDegrees[v] == 0:
                queue.append(v)    
        count = 0
        topo = []
        while queue:
            v = queue.pop(0)
            topo.append(v)
            count += 1
            for des in adjList[v]:
                inDegrees[des] -= 1
                if inDegrees[des] == 0:
                    queue.append(des)
        if count != n:
            return False  # graph has at least one cycle
        else:
            return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.topoSort(numCourses, prerequisites)
