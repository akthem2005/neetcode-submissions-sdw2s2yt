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
        s = set(d.values())
        sol = []
        count = 0
        i = 0
        a = len(nums)
        while a > 0 and count<k:
            if a in s:
                for x in d2[a]:
                    sol.append(x)
                    count +=1
            a-=1        
        return sol
