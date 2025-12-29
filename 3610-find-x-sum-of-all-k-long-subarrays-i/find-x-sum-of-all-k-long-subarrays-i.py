import heapq
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        f = {}
        for i in range(k):
            f[nums[i]] = 1 + f.get(nums[i], 0)

        out = []
        l = 0
        r = k  # FIX: treat r as the "next index to add" (window is nums[l:r])

        # FIX: loop while the current window exists; when r == len(nums) we've done the last window
        while True:
            out.append(self.window_calc(f, x))  # FIX: l/r not needed for calc

            if r == len(nums):  # FIX: stop AFTER recording the last window (no out-of-bounds)
                break

            # FIX: add nums[r] BEFORE incrementing r (your old code skipped nums[k])
            f[nums[r]] = 1 + f.get(nums[r], 0)

            # FIX: remove nums[l] and clean up zero-count keys
            f[nums[l]] -= 1
            if f[nums[l]] == 0:
                del f[nums[l]]

            l += 1
            r += 1

        return out

    def window_calc(self, f, x):
        heap = []
        for v, cnt in f.items():
            heapq.heappush(heap, (-cnt, -v))  # max by freq, then by value

        total = 0
        for _ in range(min(x, len(heap))):
            neg_cnt, neg_v = heapq.heappop(heap)
            total += (-neg_cnt) * (-neg_v)    # FIX: multiply value by its frequency
        return total
