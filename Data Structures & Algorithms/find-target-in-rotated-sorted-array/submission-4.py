class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            m = (l+r)//2
            mid = nums[m]
            first = nums[l]
            last = nums[r]

            if target == mid:
                return m
            #right sorted    
            if last >= mid:
                if mid > target >= last:
                    l = m+1
                else:
                    r = m -1
            #left sorted          
            else:
                if first <= target < mid:
                    r = m-1
                else:
                    l = m+1

        return -1                


                  



'''
 if tar == mid return mid
 if last > mid:
    --right sorted
    if mid>target>last:
        move right 
    else:
        left     

elif last < mid:
    left sorted
    if first>target>mid:
        move left
    else:
        right     


return -1
'''       
