class RandomizedSet:

    def __init__(self):
        self.h = {}
        self.nums = [] 

    def insert(self, val: int) -> bool:
        if val in self.h:
            return False
        
        self.h[val] = len(self.nums)
        self.nums.append(val)
        return True


    def remove(self, val: int) -> bool:
        if val not in self.h:
            return False 

        index = self.h[val]
        last = self.nums[-1]
        self.nums[index] = last
        self.nums.pop()
        self.h[last] = index
        del self.h[val]
        return True
 
    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()