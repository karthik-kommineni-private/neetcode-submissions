class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # right half sorted    
            if nums[m] <= nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            # left half sorted          
            else:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return -1



'''
Rotated sorted array → not fully sorted but has structure

Core idea:
→ At least one half (left or right) is always sorted

Approach:
→ Find which half is sorted
→ Check if target lies in that half
→ If yes → search there
→ Else → eliminate that half and search the other

Key trick:
→ Compare nums[mid] with nums[right]
   - nums[mid] <= nums[right] → right half sorted
   - nums[mid] > nums[right] → left half sorted

Rules:
1. Always check nums[mid] == target first

2. If right half is sorted:
   - check if target in (mid, right]
   - if yes → move left pointer (l = m + 1)
   - else → move right pointer (r = m - 1)

3. If left half is sorted:
   - check if target in [left, mid)
   - if yes → move right pointer (r = m - 1)
   - else → move left pointer (l = m + 1)

4. Always move using index (m), NOT value (nums[m])

5. Return index (m), not the value

6. Time complexity: O(log n), Space: O(1)

Mental model:
ROTATED ARRAY → ONE HALF SORTED → CHECK TARGET RANGE → ELIMINATE HALF
'''        