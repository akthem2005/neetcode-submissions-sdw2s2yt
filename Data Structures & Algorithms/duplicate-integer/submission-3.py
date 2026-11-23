class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stack = set()
        for x in nums:
            if x in stack:
                return True
            stack.add(x)
        return False