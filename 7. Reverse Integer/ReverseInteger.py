class Solution:
# Major difference between the 2, can directly multiply the sign part without needing a flag. 
# The question only asks to compare the reversed value within the range so there is no need to check the signed reversed value.
            
    def reverse(self, x: int) -> int: 
        #1.
        def reverse_2(x) :
            sign = -1 if x<0 else 1
            x *= sign
            d , rev = 0, 0
            while x:
                d = x%10
                x = x//10
                rev = rev*10 + d
            
            return 0 if rev< -2**31 or rev> 2**31 -1 else sign*rev

        return reverse_2(x)  
    # 2.     
        negative = False
        if x<0:
            negative = True
        n = abs(x)
        d , rev = 0, 0
        minInt = - (2**31 )
        maxInt = 2**31 - 1
        while n>0:
            d = n%10
            rev = rev*10 + d
            n = n//10

        if minInt<=(-rev)<=maxInt or minInt<=(rev)<=maxInt:
            if negative:
                return -rev
            else:
                return rev
        else:
            return 0
        
