class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        for x in s:
            d1[x] = d1.get(x,0)+1
        d2 = {}
        for x in t:
            if x in d1:
                d2[x] = d2.get(x,0) + 1
                if d2[x] > d1[x]:
                    return False
            else:
                return False
        return len(s) == len(t)
            