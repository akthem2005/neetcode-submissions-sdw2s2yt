class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        to_visit = set(nums)
        length = 0
        count = 1
        if nums == []:
            return 0
        while to_visit:
            x = to_visit.pop()
            c = x
            while c + 1 in to_visit:
                count +=1
                to_visit.remove(c +1)
                c +=1
            while x - 1 in to_visit:
                count +=1
                to_visit.remove(x - 1)
                x -=1
            length = max(count, length)
            count = 1
        return length