class trie_node:
    def __init__(self,):
        self.children = {}
        self.end_of_word = False
        self.count_of_word_ends = 0

class Solution:
    def __init__(self,):
        self.root = trie_node()
    
    def add_word(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = trie_node()
            cur = cur.children[char]
        cur.end_of_word = True
        cur.count_of_word_ends += 1

    def countPrefixes(self, words: List[str], s: str) -> int:
        # Using Trie
        # t: O(m+n)
        # s: O(m)
        for word in words:
            self.add_word(word)
        
        cur = self.root
        count = 0
        for char in s:
            if char in cur.children:
                cur = cur.children[char]
                if cur.end_of_word==True:
                    count+= cur.count_of_word_ends
            else:
                return count
        return count

        # Pythonic using startswith
        count = 0
        for word in words:
            if s.startswith(word):
                count+=1
        return count