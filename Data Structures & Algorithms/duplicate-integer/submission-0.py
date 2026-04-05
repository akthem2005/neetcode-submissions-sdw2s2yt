class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stack = set(nums)
        return len(stack)< len(nums)