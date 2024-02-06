class Solution:
    def reverseWords(self, s: str) -> str:
        # Approach 2
        # Faster 
        string = ""
        res = []
        for i in range(len(s)):
            if s[i]!=" ":
                string += s[i]
            elif string!="":
                res.append(string)
                string = ""
        if string!="":
            res.append(string)
        return " ".join(res[::-1])

        # Approach 1
        words = [x.strip() for x in s.split(' ') if x!='']
        #print(words)
        return ' '.join(words[::-1]).strip()