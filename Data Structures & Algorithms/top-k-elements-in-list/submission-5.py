class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for x in nums:
            d[x] = d.get(x,0) + 1
        v = {}
        for x in d:
            if d[x] in v:
                v[d[x]].append(x)
            else: v[d[x]] = [x]
        L = sorted(list(v.keys()))
        ans = []
        i = 1
        while len(ans)<k:
            for x in v[L[-i]]:
                ans.append(x)
            i+=1
        return ans