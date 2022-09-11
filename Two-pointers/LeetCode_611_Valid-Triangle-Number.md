https://leetcode.com/problems/valid-triangle-number/

```python
class Solution:
    def __init__(self):
        self.result = 0
        
    def triangleNumber(self, nums: List[int]) -> int:
        if not nums or len(nums)<3:
            return self.result
        nums.sort() # O(nlog(n))
        # let basis be the largest of three
        for i in range(2, len(nums)): # O(n^2)
            left = 0
            right = i-1
            basis = nums[i] # left + right > basis
            self.twoSumBiggerCalc(nums, left, right, basis)
        return self.result
            
    def twoSumBiggerCalc(self, nums: List[int], left: int, right: int, basis: int):
        while left < right:
            if (nums[left] + nums[right] > basis):
                self.result += (right - left)
                right -= 1
            else: # nums[left] + nums[right] <= basis
                left += 1
```
#### Remark:
- Similar to [Leet259](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_259_3Sum-Smaller.md), just in opposite direction. 
#### Submission:
```
Runtime: 3088 ms, faster than 26.28% of Python3 online submissions for Valid Triangle Number.
Memory Usage: 14 MB, less than 29.95% of Python3 online submissions for Valid Triangle Number.
```
#### Complexity:
- Time: O(nlogn) + O(n^2)
- Space: O(1)
