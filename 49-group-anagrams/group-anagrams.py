class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                index = ord(c) - ord('a')
                count[index] += 1
            count = tuple(count)
            h[count].append(word)

        return list(h.values())