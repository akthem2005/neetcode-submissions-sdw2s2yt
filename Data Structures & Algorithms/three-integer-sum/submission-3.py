class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        L = sorted(nums)
        a = 0
        ans = []
        while a<len(nums)-2:
            i = len(nums)-1
            b = a+1
            while b<i:
                num = L[a]+L[b]
                if num+L[i]<0:
                    x = L[b]
                    while L[b] == x and b<i:
                        b+=1
                elif num+L[i]>0:
                    y = L[i]
                    while L[i] == y and b<i:
                        i-=1
                else:
                    ans.append([L[i], L[a], L[b]])
                    y = L[i]
                    while L[i] == y and b<i:
                        i-=1
                    x = L[b]
                    while L[b] == x and b<i:
                        b+=1
            z = L[a]
            while L[a] == z and a< len(nums)-2:
                a+=1
        return ans
