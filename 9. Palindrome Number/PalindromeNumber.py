class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Don't have to worry about the case when x<0 because if its negative then the sign will always come to the end making it false
        # xstr = [s for s in str(x)]
        # left, right = 0, len(xstr)-1
        # temp = ''

        # while right>=left:
        #     xstr[left], xstr[right] = xstr[right], xstr[left]
        #     left+=1
        #     right-=1
        
        # return str(x) == ''.join(xstr)

        if x<0:
            return False
        n = x
        d, rev = 0, 0
        while n:
            d = n%10
            n=n//10
            rev = rev*10 + d
        
        return rev == x 