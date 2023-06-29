class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        print(words)
        
        return len(words[-1])