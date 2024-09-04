class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not endWord or not beginWord or not wordList or endWord not in wordList \
		or beginWord == endWord:
            return []

        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        # Build graph, bi-BFS
        # ans = []
        bqueue = collections.deque()
        bqueue.append(beginWord)
        equeue = collections.deque()
        equeue.append(endWord)
        bvisited = set([beginWord])
        evisited = set([endWord])
        rev = False 
        #graph
        parents = collections.defaultdict(set)
        found = False 
        depth = 0
        while bqueue and not found:
            depth += 1 
            length = len(bqueue)
            # print(queue)
            localVisited = set()
            for _ in range(length):
                word = bqueue.popleft()
                for i in range(L):
                    for nextWord in all_combo_dict[word[:i] + "*" + word[i+1:]]:
                        if nextWord == word:
                            continue
                        if nextWord not in bvisited:
                            # rev means that were starting from endword and tryign to build start word. so that would mean that new_word is closer to startword and so the key becomes the new word and word becomes its value i.e from new_word we can form word
                            if not rev:
                                parents[nextWord].add(word)
                            else:
                                parents[word].add(nextWord)
                            if nextWord in evisited:    
                                found = True
                            localVisited.add(nextWord)
                            bqueue.append(nextWord)
            bvisited = bvisited.union(localVisited)
            bqueue, bvisited, equeue, evisited, rev = equeue, evisited, bqueue, bvisited, not rev
        # print(parents)
        # print(depth)
        # Search path, DFS
        # path will contain the paths from one word to another which will ultimately lead to the endword. so we need to find all the paths and they will be the shortest as path was stopped filling after finding the shortest path
        ans = []
        def dfs(node, path, d):
            if d == 0:
                if path[-1] == beginWord:
                    ans.append(path[::-1])
                return 
            for parent in parents[node]:
                path.append(parent)
                dfs(parent, path, d-1)
                path.pop()
        dfs(endWord, [endWord], depth)
        return ans


        # Leads to MLE

        # Each word is a pattern
        # hot -> *ot, h*t, ho* 
        # hit -> *it, h*t, hi*
        # h*t can represent both hot and hit, so transformation is possible
        # h*t : [hot, hit]
        # *ot: [hot, dot]

        # BFS to find the shortest path from begining word to ending word based on similar patterns created between words
        wordList = set(wordList)
        if endWord not in wordList:
            return []
            
        # wordList.add(beginWord)
        patterns = collections.defaultdict(list)
        for word in wordList:
            for index in range(len(word)):
                pattern = word[:index] + "*" + word[index+1:]
                patterns[pattern].append(word)
        
        # print("patterns=", patterns)
        
        queue = collections.deque([(beginWord, [beginWord])])
        visited = set()
        visited.add(beginWord)
        word_found = False
        ans = []
        while queue and not ans:
            # print("queue=", queue)
            local_visited = set()
            for _ in range(len(queue)):
                word, path = queue.popleft()
                # print("word={} path={}".format(word, path))

                for index in range(len(word)):
                    pattern = word[:index] + "*" + word[index+1:]
                    for next_word in patterns[pattern]:
                        # print("next_word=", next_word)
                        if next_word==endWord:
                            word_found=True
                            ans.append(path+[next_word])
                        if next_word not in visited:
                            local_visited.add(next_word)
                            queue.append((next_word, path+[next_word]))
            
            visited = visited.union(local_visited)
                   
        return ans