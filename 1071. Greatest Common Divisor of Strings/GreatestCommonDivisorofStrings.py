class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        for i in range(min(len(str1), len(str2)), 0, -1):
            if( l1%i!=0 or l2%i!=0):
                continue
            elif( str1 == (str1[:i]*(l1//len(str1[:i]))) and
                    str2 == (str1[:i]*(l2//len(str1[:i])))):
                    return str1[:i]
        return ""