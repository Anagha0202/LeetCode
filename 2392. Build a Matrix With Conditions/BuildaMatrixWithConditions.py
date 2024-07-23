class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Approach: Topological sort 
        # Topological sort is used for directed acyclic graphs to order the vertices (u,v) such that u always appears before v. 
        # Uses a visited set and stack data structures. 
        # Time: O(n+m)
        # Space: O(n*m)
        ans = [[0]*k for _ in range(k)]
        rowGraph, colGraph = defaultdict(list), defaultdict(list)
        # Adjacency list for each condition - graph
        for u,v in rowConditions:
            rowGraph[u].append(v)
        for u,v in colConditions:
            colGraph[u].append(v)
        
        def topSortHelper(vertex, visited, stack, path, graph):
            if vertex in path:
                return False
            if vertex in visited:
                return True
            
            visited.add(vertex)
            path.add(vertex)
            for v in graph[vertex]:
                if not topSortHelper(v, visited, stack, path, graph):
                    return False
            stack.append(vertex)
            path.remove(vertex)
            return True
        
        def topSort(graph):
            visited, stack, path = set(), [], set()
            for v in range(1,k+1,1):
                if not topSortHelper(v, visited, stack, path, graph):
                    return []
            return stack[::-1]
        
        rowOrder = topSort(rowGraph)
        colOrder = topSort(colGraph)
        if not rowOrder or not colOrder:
            return []

        pos = {n:[0,0] for n in range(1,k+1,1)}
        for i, n in enumerate(rowOrder):
            pos[n][0] = i
        for j, n in enumerate(colOrder):
            pos[n][1] = j
        for n in range(1, k+1, 1):
            i, j = pos[n]
            ans[i][j] = n
        return ans