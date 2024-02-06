class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = collections.defaultdict(list)
        for s in strs:
            temp = ''.join(sorted(s))
            sorted_strs[temp].append(s)        
        # print(list(sorted_strs.values()))
        return list(sorted_strs.values())