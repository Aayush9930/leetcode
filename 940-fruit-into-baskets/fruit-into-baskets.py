class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        l = 0
        res = 0
        
        for r, x in enumerate(fruits):
            count[x] += 1
            
            # shrink window if we have more than 2 types
            while len(count) > 2:
                left_fruit = fruits[l]
                count[left_fruit] -= 1
                if count[left_fruit] == 0:
                    del count[left_fruit]
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
            
                    
                    
