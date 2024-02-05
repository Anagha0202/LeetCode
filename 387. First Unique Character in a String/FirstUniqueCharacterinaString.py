class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = dict(collections.Counter(s))

        for ch, count in chars.items():
            if count==1:
                return s.index(ch) # will work because index return the first instance of the item
        return -1