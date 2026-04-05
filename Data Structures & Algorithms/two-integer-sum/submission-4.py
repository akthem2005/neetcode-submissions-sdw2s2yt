class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, x in enumerate(nums):
            if target- x in d:
                return [min(d[target-x],i), max(d[target-x],i)]
            else:
                d[x] = i
