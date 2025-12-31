class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        f = {}

        for x in nums:
            # blindly adding
            f[x] = 1 + f.get(x, 0)

            # cleaning up extra elements
            if  len(f) > 2:
                remove_elements = []
                for val in f:
                    f[val] -= 1
                    if f[val] == 0:
                        remove_elements.append(val)

                for val in remove_elements:
                    del f[val]
                
        if len(f) == 0:
            return []
        
        out = []
        for val in f:
            x = nums.count(val)
            if x > len(nums) // 3:
                out.append(val)

        return out

        
        # f = {}

        # for x in nums:
        #     f[x] = 1 + f.get(x, 0)
        
        # out = []
        # for x in f:
        #     if f[x] > len(nums) // 3:
        #         out.append(x)
        
        # return out
         