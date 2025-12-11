import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        h = {}

        for word in words:
            h[word] = 1 + h.get(word, 0)
        
        a = []
        for word in h:
            heapq.heappush(a, (-h[word], word))
        out = []
        for _ in range(k):
            f, word = heapq.heappop(a)
            out.append(word)
        
        return out
        
