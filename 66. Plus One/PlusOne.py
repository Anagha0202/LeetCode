class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        i = 0
        val = 1
        flag = True
        while flag and i<len(digits):
            tempsum = digits[i]+val
            if tempsum>9:
                digits[i] =  tempsum%10
                val = tempsum//10
                i +=1
            else:
                digits[i] = tempsum
                flag = False
        if flag:
            digits.append(val)
        digits.reverse()
        return digits     