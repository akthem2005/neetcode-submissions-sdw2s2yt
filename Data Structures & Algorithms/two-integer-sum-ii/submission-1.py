class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers)-1
        while b>a:
            if numbers[b]+numbers[a] > target:
                b-=1
            elif numbers[b]+numbers[a] < target:
                a+=1
            else:
                return [a+1,b+1]
