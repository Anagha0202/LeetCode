class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)<len(s) or len(t)>len(s):
            return False
        # Approach 3: Hashtable as Array
        # Time: O(n)
        # Space: O(n)
        counts = defaultdict(int)
        for x in s:
            counts[ord(x) -ord('a')] += 1
        
        for y in t:
            if counts[ord(y) - ord('a')] == 0: 
                return False
            counts[ord(y) - ord('a')] -= 1

        return not sum(counts.values())>0 

        # Approach 2: Sorting
        # Time: O(n log n)
        # Space: O(1)
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i]!=t[i]:
                return False
        return True

        # Approach 1: Hashtable
        # Time: O(n+m)
        # Space: O(n+m)

        countS = Counter(s)
        countT = Counter(t)

        return countS==countT
        # OR
        for ch in countS:
            if ch not in countT or countS[ch]!=countT[ch]:
                return False
        return True