class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for x in strs:
            if ''.join(sorted(x)) in d:
                d[''.join(sorted(x))].append(x)
            else: d[''.join(sorted(x))] = [x]
        return list(d.values())