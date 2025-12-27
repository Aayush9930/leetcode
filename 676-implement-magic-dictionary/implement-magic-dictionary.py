class MagicDictionary:

    def __init__(self):
        self.h = defaultdict(list) 

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                self.h[pattern].append(word)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            pattern = searchWord[:i] + "*" + searchWord[i + 1:]
            if self.h[pattern] != []:
                if len(self.h[pattern]) == 1 and self.h[pattern][0] == searchWord:
                    continue
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)