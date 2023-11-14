class Solution:
    def compress(self, chars: List[str]) -> int:

        count = 1
        for i in range(len(chars)-1, 0, -1):
            if chars[i] == chars[i-1]:
                count+=1
            else:
                if count>1:
                    chars[i:i+count] = chars[i+1] + str(count) 
                    count = 1
        if count>1:
            chars[0:0+count] = chars[0+1] + str(count)

        return len(chars)
        