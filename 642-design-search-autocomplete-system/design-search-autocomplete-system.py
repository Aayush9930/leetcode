import heapq
from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = []  # heap of (-freq, sentence)

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.currSentence = ""
        self.currPointer = self.root
        self.freq = defaultdict(int)

        for s, t in zip(sentences, times):
            self.freq[s] += t
            self._insert(s)

    def _insert(self, s: str):
        node = self.root
        for ch in s:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            heapq.heappush(node.sentences, (-self.freq[s], s))  # push current freq

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.freq[self.currSentence] += 1
            self._insert(self.currSentence)
            self.currSentence = ""
            self.currPointer = self.root
            return []

        # ALWAYS build the current sentence
        self.currSentence += c

        # If path doesn't exist yet, create it and return []
        if c not in self.currPointer.children:
            self.currPointer.children[c] = TrieNode()
            self.currPointer = self.currPointer.children[c]
            return []

        self.currPointer = self.currPointer.children[c]
        heap = self.currPointer.sentences

        res = []
        popped = []
        while heap and len(res) < 3:
            f, s = heapq.heappop(heap)
            # discard stale entries
            if -f != self.freq[s]:
                continue
            res.append(s)
            popped.append((f, s))

        # put back the valid ones we popped
        for item in popped:
            heapq.heappush(heap, item)

        return res
