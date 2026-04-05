class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,x in enumerate(nums):
            d[x] = (i,d.get(x, (0,0))[1]+1)
        for i,x in enumerate(nums):
            if target- x in nums:
                if x == target-x:
                    if d[target-x][1] >1:
                        return [i,d[x][0]]
                else:
                    return [i,d[target-x][0]]

