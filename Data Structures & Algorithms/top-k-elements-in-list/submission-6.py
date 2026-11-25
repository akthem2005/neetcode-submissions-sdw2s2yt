class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1
        t = {}
        for x in d:
            if d[x] not in t:
                t[d[x]] = [x]
            else:
                t[d[x]].append(x)
        freq = sorted(list(t.keys()))
        i = 0
        a = 1
        L = []
        while i<k:
            for x in t[freq[-a]]:
                L.append(x)
            i+=len(t[freq[-a]])
            a+=1
            
        return L