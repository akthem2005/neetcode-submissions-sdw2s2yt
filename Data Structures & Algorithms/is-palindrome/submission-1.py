class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) ==1:
            return True
        clean = [x.lower() for x in s if x.isalnum()]
        a = 0
        b = len(clean)-1
        while b>a:
            if clean[a] != clean[b]:
                return False
            a+=1
            b-=1
        return True