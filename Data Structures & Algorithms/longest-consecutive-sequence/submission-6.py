class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        to_visit = set(nums)
        length = 0
        for x in to_visit:
            if x-1 not in to_visit:
                c = x
                count = 1
                while c+1 in to_visit:
                    count +=1
                    c+=1
                length = max(length, count)
        return length
