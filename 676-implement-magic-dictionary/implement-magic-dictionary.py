class MagicDictionary:

    def __init__(self):
        self.patterns = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.patterns[word] = set()
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                self.patterns[word].add(pattern)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            pattern = searchWord[:i] + "*" + searchWord[i + 1:]
            for word in self.patterns:
                if word != searchWord:
                    if pattern in self.patterns[word]:
                        return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)