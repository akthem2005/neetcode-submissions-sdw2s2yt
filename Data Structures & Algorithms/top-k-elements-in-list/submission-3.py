class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for x in nums:
            d[x] = d.get(x,0)+1
        d2={}
        for x in d:
            if d[x] in d2:
                d2[d[x]].append(x)
            else: d2[d[x]] = [x]
        L = sorted(list(set(d.values())), reverse = True)
        sol = []
        count = 0
        i = 0
        while count < k:
            for x in d2[L[i]]:
                sol.append(x)
                count +=1
            i+=1
        return sol
