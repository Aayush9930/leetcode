class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # O(1) -> only possible with bit ops if i need O(n)
        ans = 0
        for num in nums:
            ans = ans ^ num 
        
        return ans