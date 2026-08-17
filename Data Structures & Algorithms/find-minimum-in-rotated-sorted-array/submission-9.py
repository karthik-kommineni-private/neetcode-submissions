class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1

        while i < j:
            m = (i + j) // 2

            if nums[m] > nums[j]:
                i = m + 1
            else:
                j = m

        return nums[i]



'''
Rotated sorted array → not fully sorted but has structure

Core idea:
→ At least one half is always sorted
→ Use this to eliminate half of the search space

Goal:
→ Find the minimum element (pivot)

Key trick:
→ Compare nums[mid] with nums[right]
   - nums[mid] > nums[right] → min is in RIGHT half
   - nums[mid] <= nums[right] → min is in LEFT half (including mid)

Approach:
1. If mid > right → discard left half → i = m + 1
2. Else → discard right half → j = m (keep mid)

Important rules:
3. Use while i < j (NOT i <= j)
   - when i == j, we already found the answer
   - using <= can cause infinite loop

4. Always move using index (m), not value

5. Do NOT compare with left boundary → less reliable
   → comparing with right gives clear pivot direction

6. Avoid using m+1 / m-1 → prevents boundary issues

7. Final position i == j → points to minimum

Mistake I made:
→ Used while i <= j
→ This can cause infinite loop because j = m does not shrink range when i == j

Complexity:
→ Time: O(log n)
→ Space: O(1)

Mental model:
ROTATED ARRAY → COMPARE MID WITH RIGHT → DISCARD HALF → LAND ON MIN
'''        