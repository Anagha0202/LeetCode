from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        """
        has not been run and checked 
        ["wrt","wrf","er","ett","rftt"]
        w -> r -> t, f => t<f {t:f}
        e -> r, t => r<t {r:t}
        r -> f -> t 
        => r<t<f
        => w<e<r 
        ~ w<e<r<t<f {w:e, e:r, r:t, t:f}

        take 2 strings, 
        find the longest prefix between them, 
        char at prefix+1 in both strings determines the order of those 2 characters
        Add to a hashmap smaller:larger {t:f}
        Topological Order
        traverse the hashmap using dfs, visited set and path in post order traversal, 
        if cycle detected i.e node in path, return True that loop was detected
        if a node was already visited, return False as not a loop
        add char to path 

        while finding the prefix using 2 pointer, 
        if we reach the end of a string2, prefix is following string1, return ""

        return the topologiacl order in reverse order
        """
        order = {}
        for index in range(len(words)-1):
            string1, string2 = words[index], words[index+1]
            min_len = min(len(string1), len(string2))
            # string2 needs to be longer than string 1 else invalid
            # if entire string2 is a prefix of string1, then invalid 
            # because shorter string2 should have come before string1 in dict
            if len(string2)<len(string1) and string2[:min_len]==string1[:min_len]:
                return ""
            
            # traverse over the characters in the strings for min_len 
            # if differing character is found, add it in correct order to order dict 
            for j in range(min_len):
                if string1[j]!=string2[j]:
                    order[string1[j]].add(string2[j])
                    break
        
        visited = set()
        topo_order = []
        path = set()
        def traverse_order(char, path, visited):
            if char in path:
                return True
            if char in visited:
                return False

            visited.add(char)
            path.add(char)
            # visit a char by adding all its children and then itself
            for next_char in order[char]:
                if traverse_order(next_char, path, visited): # loop found
                    return True
            topo_order.append(char)
            path.remove(char)
            return False

        for char in order:
            if traverse_order(char, path, visited):
                return ""
        
        return ''.join(topo_order[::-1])
        

