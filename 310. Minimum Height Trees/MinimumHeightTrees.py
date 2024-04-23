class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Topological Sorting - altering tree based on in-degree and out-degree of each node
        # From root to lowest leaf is the height of tree
        # Imagining a tree where the root starts from the center, 
        # we traverse from the leaves towards the root. (Eat up all leaves until the center 1 or 2)
        # Because a leave will not have adjacent edges, so cannot be the root.
        # While traversing, remove an edge that we have seen.

        adj = collections.defaultdict(set)
        for src,dest in edges:
            adj[src].add(dest)
            adj[dest].add(src)
        
        leaves = [x for x in range(0,n) if len(adj[x])<=1]

        while n>2 :
            # remove leaves from original tree 
            n -= len(leaves)
            templeaves = []
            for l1 in leaves:
                l2 = adj[l1].pop()
                adj[l2].remove(l1)
                if len(adj[l2]) == 1:
                    templeaves.append(l2)
            leaves = templeaves
        return leaves