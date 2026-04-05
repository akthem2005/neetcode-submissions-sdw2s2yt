class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p1 = [0] * n
        p2 = [0] * n
        for i in range(0,n):
            if i==0:
                p1[i] = nums[0]
                p2[-i-1] = nums[-1]
            else:
               p1[i] = p1[i-1]* nums[i]
               p2[-i-1] = p2[-i] * nums[-i-1]
        
        L = [0]*n
        for i in range(len(nums)):
            if i==0:
                L[i] = p2[1]
            elif i == n-1:
                L[i] = p1[n-2]
            else:
                L[i] = p1[i-1]* p2[i+1]
        return L