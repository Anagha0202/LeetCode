class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        brackets = {')':'(', '}':'{', ']':'['}
        stack = []
        for x in s:
            if x in brackets.keys():
                if not stack or stack.pop()!=brackets[x]:
                    return False
            else:
                stack.append(x)
        return not stack        