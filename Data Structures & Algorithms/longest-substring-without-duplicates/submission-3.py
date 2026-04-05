class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        a = 0
        b = 1
        l = {s[0]:0}
        size = 0
        while b < len(s):
            
            if s[b] in l and l[s[b]]>=a:
                size = max(b-a,size)
                a=l[s[b]]+1
                l[s[b]]=b
                b+=1
            else:
                l[s[b]]=b
                b+=1
            print(a,b)
        return max(size,b-a)