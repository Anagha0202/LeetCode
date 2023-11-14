class Solution:
    def reverseParentheses(self, s: str) -> str:
        # stack => ( e d ( e t ( o c
        #       => ( e d ( e t c o
        #       => ( e d o c t e e l
        #       => l e e t c o d e

        # Time: O(n)
        # Space: O(n)
        
        stack = []

        for ch in s:
            if ch == ')':
                temp = []
                while stack[-1]!='(':
                    temp.append(stack.pop())
                    # print("temp=", temp)
                stack.pop()
                stack.extend(temp)
                # print("new stack=", stack)
            else:
                stack.append(ch)
            # print("stack=", stack)
        
        res = ''.join(stack)
        return res

        