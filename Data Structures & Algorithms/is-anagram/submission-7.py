class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        l = {}
        for c in t:
            l[c] = l.get(c, 0) + 1
        
        for x in d:
            if x not in l:
                return False
            if d[x]!=l[x]:
                return False
        return True
        