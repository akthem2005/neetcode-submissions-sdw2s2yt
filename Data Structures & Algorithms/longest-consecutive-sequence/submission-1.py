class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        to_visit = set(nums)
        length = set()
        count = 1
        if nums == []:
            return 0
        while to_visit:
            mini = min(to_visit)
            to_visit.remove(mini)
            while mini +1 in to_visit:
                count +=1
                to_visit.remove(mini +1)
                mini +=1
            length.add(count)
            count = 1
        return max(length)