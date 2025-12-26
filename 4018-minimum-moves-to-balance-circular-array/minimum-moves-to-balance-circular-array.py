class Solution:
    def minMoves(self, balance: List[int]) -> int:

        n = len(balance)

        if sum(balance) < 0:
            return -1

        culpritIdx = None
        for i in range(len(balance)):
            if balance[i] < 0:
                culpritIdx = i 
                break
        
        if culpritIdx == None:
            return 0
        
        distance = 1 
        moves = 0
        need = -balance[culpritIdx]

        while need != 0:
            leftIdx = (culpritIdx - distance + n) % n
            rightIdx = (culpritIdx + distance) % n

            if leftIdx == rightIdx:
                units = min(need, balance[leftIdx])
                need -= units
                moves += units * distance
                distance += 1
            
            else:
                units = min(need, balance[leftIdx] + balance[rightIdx])
                need -= units
                moves += units * distance
                distance += 1
        
        return moves
         
        
