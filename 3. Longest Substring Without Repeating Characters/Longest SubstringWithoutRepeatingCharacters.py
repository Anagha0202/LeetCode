class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0

        # Using 2 pointer to traverse and hasmap of indexes to maintain window chars
        # t: O(n)
        # s: O(n)
        left, right = 0, 0
        char_seen_indexes = {}
        max_len = 0
        while right<len(s):
            if s[right] in char_seen_indexes and left<char_seen_indexes[s[right]]+1 :
                left = char_seen_indexes[s[right]] + 1
            max_len = max(max_len, right-left+1)
            char_seen_indexes[s[right]] = right
            right+=1

        return max_len
        
        # Using Queue to maintain the window
        # t: O(n)
        # s: O(n)
        unique_chars = collections.deque()
        max_len = 0
        for char in s:
            if char in unique_chars:
                max_len = max(max_len, len(unique_chars))
                while unique_chars.popleft()!=char:
                    continue
            unique_chars.append(char)
        
        if unique_chars:
            max_len = max(max_len, len(unique_chars))
        return max_len