class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Approach 1: Union Find 
        # Time: O(nlogn)
        # space: O(n)
        parent = {}
        email_name = {}

        def findParent(n):
            while parent[n] != n:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n
        
        def union(n1, n2):
            p1 = findParent(n1)
            p2 = findParent(n2)
            if p1!=p2:
                parent[p1] = p2
        
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_name[email] = name
                union(email, account[1])
        
        emails = defaultdict(list)
        for e in parent.keys():
            emails[findParent(e)].append(e)
        
        return [[email_name[root]] + sorted(email) for (root, email) in emails.items()]