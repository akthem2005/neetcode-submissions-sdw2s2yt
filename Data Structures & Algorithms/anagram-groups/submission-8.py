class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for x in strs:
            L = [0]*26
            for c in x:
                L[ord(c)-97]+=1
            if str(L) in d:
                d[str(L)].append(x)
            else:
                d[str(L)] = [x]
        return list(d.values())