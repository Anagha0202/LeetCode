class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Basic Brute Force:
        # compare each word in words with s and find if it is a subsequence using greedy two pointer method and return the largest word
        # A bit optimized Brute Force:
        # Max heap to provide the longest strings first and greedily check if subsequence 
        # t: O(n*m)
        # s: O(n)

        # Procesing by Buckets
        # approach is to compare a character in s, s[i] with character present at i all words. 
        # Preprocess words based on the first character which gives dictionary where words are sorted based on first character and the first character is the key. 
        # Iterate over S. for each character s[i] process word dict[s[i]] and remove the first character from all the words and regroup based on the current first character. This means that first character in all those words has been found in S hence until that index, the word can be made. 
        # When the word is emptied i.e. removing the first characters led to empty string, => word has been found and count can be incremented
        # t: O(n+m) 
        # s: O(m)

        word_bucket = collections.defaultdict(list)
        for word in words:
            word_bucket[word[0]].append(word)
        
        count = 0
        for index, char in enumerate(s):
            word_list = word_bucket[char]
            word_bucket[char] = []
            while word_list:
                word = word_list.pop()
                new_word = word[1:]
                if new_word=="":
                    count+=1
                    continue
                word_bucket[new_word[0]].append(new_word)
        return count

    # Google question:
        # Follow up: return the longest word that is a subsequence of S

        word_bucket = collections.defaultdict(list)
        for index, word in enumerate(words):
            word_bucket[word[0]].append((word, len(word), index))
        
        max_length = 0
        longest_word = ""
        for index, char in enumerate(s):
            word_list = word_bucket[char]
            word_bucket[char] = []
            while word_list:
                (word, length, original_index) = word_list.pop()
                new_word = word[1:]
                if new_word=="":
                    if length>max_length:
                        max_length = length
                        longest_word = words[original_index]
                    continue
                word_bucket[new_word[0]].append((new_word, length, original_index))
        return longest_word