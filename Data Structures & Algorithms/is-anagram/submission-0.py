class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1

        d2 = {}
        for c in t:
            d2[c] = d2.get(c, 0) + 1
        for x in d:
            if x not in d2:
                return False
            if d[x]!=d2[x]:
                return False
        return True