class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        h = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                h[pattern].append(word)
        
        q = deque([(beginWord, 1)])
        visited = set()

        while q:
            word, l = q.popleft()

            if word in visited:
                continue

            if word == endWord:
                return l 
            
            visited.add(word)

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                for n in h[pattern]:
                    if n != word:
                        q.append((n, l + 1))
        
        return 0
