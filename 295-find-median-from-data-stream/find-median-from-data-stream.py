import heapq
class MedianFinder:
    def __init__(self):
        self.small = [] # max heap
        self.big = [] # min heap

    def addNum(self, num: int) -> None:
        # add the num to the small 
        heapq.heappush(self.small, -num) # logn

        # check if my definitions are still correct
        if self.small and self.big and -self.small[0] > self.big[0]:
            val = heapq.heappop(self.small) # neg  O(1)
            heapq.heappush(self.big, -val)  # logn

        # are they balanced??
        if len(self.big) > len(self.small) + 1:
            val = heapq.heappop(self.big)
            heapq.heappush(self.small, -val)# logn
        
        if len(self.big) + 1 < len(self.small):
            val = heapq.heappop(self.small)
            heapq.heappush(self.big, -val)# logn


    def findMedian(self) -> float:
        if len(self.big) == len(self.small):
            return (self.big[0] + (-self.small[0])) / 2 
        
        if len(self.big) < len(self.small):
            return -self.small[0]

        if len(self.small) < len(self.big):
            return self.big[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()