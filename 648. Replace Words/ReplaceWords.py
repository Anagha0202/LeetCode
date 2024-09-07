class trie_node:
    def __init__(self, ):
        self.children = {}
        self.end_of_word = False

class Solution:
    def __init__(self, ):
        self.root = trie_node()
    
    def add_word(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = trie_node()
            cur = cur.children[char]
        cur.end_of_word = True
    
    def search_prefix(self, word):
        cur = self.root
        prefix = ""
        for char in word:
            if char not in cur.children:
                return word
            prefix+=char
            if cur.children[char].end_of_word:
                return prefix
            cur = cur.children[char]
        return word

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        dict - roots => prefixes of derivatives
        root + word = derivative
        cat + tle = cattle
        rat + tled = rattled
        bat + tery = battery

        sentence len [1,1000]
        sentence word len [1, 1000]

        Approach 1: 
        take each word in sentence, 
        take substring of len= 1,2..n,
        see if the prefix exists in the dict, 
        track the prefix length and prefix word,
        replace it by the shortest one
        t: O(longest word*n)
        s: O(1)

        Approach 2:
        take each word in prefixes/dict, 
        go over the sentence, 
        take substring of each word of length prefix and compare, 
        compare length of word with prefix and replace, 
        t: O(m*n)
        s: O(1)

        Optimal Approach: 
        Tries - prefix Tree
        convert dict (prefixes) into a Trie
        end of each word, mark as end of word
        go over sentence by word and char
        if char not in trie, skip to next word
        if char in trie and is end of word, replace word with prefix
        Using trie ensures that you will encounter smallest prefix first
        t: O(m+n) - O(length of root of trie*no of prefixes + longest word*len of sentence)
        s: O(length of trie + length of sentence)
        """
        for prefix in dictionary:
            self.add_word(prefix)
        
        words = sentence.split(" ")
        for index,word in enumerate(words):
            replacement = self.search_prefix(word)
            # print(word, replacement)
            words[index] = replacement
        return " ".join(words)