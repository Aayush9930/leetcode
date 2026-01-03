import heapq
from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = []  # heap of (-freq, sentence)

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.currSentence = ""
        self.currPointer = self.root
        self.freq = defaultdict(int)   # <-- add frequency map

        for i in range(len(sentences)):
            self.addSentence(sentences[i], times[i])  # now "f" is a delta

    def addSentence(self, s, f):
        # f is delta; keep true total in freq
        self.freq[s] += f
        total = self.freq[s]

        curr = self.root
        for c in s:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

            # Option A update: remove old entries for s, then push updated one
            if curr.sentences:
                curr.sentences = [(negf, sent) for (negf, sent) in curr.sentences if sent != s]
                heapq.heapify(curr.sentences)
            heapq.heappush(curr.sentences, (-total, s))

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.addSentence(self.currSentence, 1)
            self.currSentence = ""
            self.currPointer = self.root
            return []

        # IMPORTANT: always advance the current sentence
        self.currSentence += c

        # if path doesn't exist, create it and return []
        if c not in self.currPointer.children:
            self.currPointer.children[c] = TrieNode()
            self.currPointer = self.currPointer.children[c]
            return []

        # move pointer
        self.currPointer = self.currPointer.children[c]

        a = self.currPointer.sentences
        out = []
        popped = []

        for _ in range(3):
            if not a:
                break
            item = heapq.heappop(a)
            popped.append(item)
            out.append(item[1])

        for item in popped:
            heapq.heappush(a, item)

        return out
