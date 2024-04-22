class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target=="0000":
            return 0

        dirs = [[1,0,0,0], [-1,0,0,0],
                [0,1,0,0], [0,-1,0,0],
                [0,0,1,0], [0,0,-1,0],
                [0,0,0,1], [0,0,0,-1]]
        visited = set(("0000"))
        deadend = set(deadends)
        queue = collections.deque([("0000", 0)])

        if target in deadends or "0000" in deadends:
            return -1

        while queue:
            node, count = queue.popleft()
            visited.add(node)
            print("node: {} count: {}".format(node, count))
            if node==target:
                return count
            if node in deadends:
                continue
            for [d1,d2,d3,d4] in dirs:
                t1 = str(((int(node[0])+d1) + 10)%10)
                t2 = str(((int(node[1])+d2) + 10)%10)
                t3 = str(((int(node[2])+d3) + 10)%10)
                t4 = str(((int(node[3])+d4) + 10)%10)
                t = t1+t2+t3+t4
                if t not in visited and t not in deadend:
                    queue.append((t, count+1))
                    visited.add(t)
        return -1