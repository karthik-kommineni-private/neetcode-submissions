class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        L,R = 0, len(numbers)-1

        while L < R:

            s = numbers[L] + numbers[R]

            if  s == target and L < R:
                return [L+1,R+1]
            
            if s > target:
                R-=1
            else:
                L+=1



        