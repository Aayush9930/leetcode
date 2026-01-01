from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque([("0000", 0)])
        visited = set()
        deadends = set(deadends)

        while q:
            c, l = q.popleft()

            if c in visited:
                continue
            
            if c in deadends:
                continue

            if c == target:
                return l
            
            visited.add(c)

            for n in self.getNeighbors(c):
                q.append((n, l + 1))    
        
        return -1
    
    def getNeighbors(self, comb):
        out = []

        for i in range(len(comb)):
            c = int(comb[i])
            nxt = str((c + 1) % 10)
            prev = str((c - 1 + 10) % 10)
            out.append(comb[:i] + nxt + comb[i + 1:])                    # (c + 1) % 10
            out.append(comb[:i] + prev + comb[i + 1:])                    # (c - 1 + 10) % 10

        return out        

