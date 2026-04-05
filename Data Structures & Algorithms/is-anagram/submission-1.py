class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        d = {}
        d2 = {}
        for c in s:
            d[c] = d.get(c, 0) + 1

        
        for c in t:
            d2[c] = d2.get(c, 0) + 1
        
        return d == d2