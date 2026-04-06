class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        a = 0
        b = 1
        ans = 0
        d = {s[0]: 1}
        big = s[0]
        while a < len(s) and b< len(s):
            d[s[b]] = d.get(s[b],0)+1
            if d[s[b]]> d[big]:
                big = s[b]
            change = sum([d[x] for x in d if x != big])
            if change > k:
                d[s[a]]-=1
                a+=1
            ans = max(ans, b-a+1)
            b+=1
        return ans
