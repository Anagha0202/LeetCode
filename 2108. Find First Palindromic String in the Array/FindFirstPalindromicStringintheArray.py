class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # Pythonic
        for string in words:
            if string == string[::-1]:
                return string
        return "" 
        # Algorithmic:
        for string in words:
            i, j = 0, len(string)-1
            while i<=j:
                if string[i]!=string[j]:
                    break
                i+=1
                j-=1
            if i<=j:
                continue
            else:
                return string
        return ""