# 208. Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Approach:
-using a prefix tree
-create a tree for each word
-root will have 26 branches, 1 for each starting character
-when inserting new word, go letter by letter and check if common letters then go down the branch, else create a new node
-when inserting new word, once you reach the last character, mark it as the end of the word