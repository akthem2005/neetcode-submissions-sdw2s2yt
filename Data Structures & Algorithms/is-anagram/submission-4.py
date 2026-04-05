class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for x in s:
            d1[x] = d1.get(x,0)+1
        for x in t:
            if x not in d1:
                return False
            d2[x] = d2.get(x,0)+1
        for x in s:
            if x not in d2:
                return False
            if d1[x]!=d2[x]:
                return False
        return True