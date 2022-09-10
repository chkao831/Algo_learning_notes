https://leetcode.com/problems/3sum-smaller/submissions/

```python
class Solution:
    def __init__(self):
        self.result = 0
    
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        if not nums or len(nums)<3:
            return self.result
        
        nums.sort() #nlog(n)
        for i in range(0, len(nums)-2):
            left = i+1
            right = len(nums)-1
            quota = target - nums[i] # basis + two_sum < target => target - basis = quota > two_sum => 2Sum Smaller
            self.twoSumSmallerCalc(nums, left, right, quota)
        return self.result
            
    def twoSumSmallerCalc(self, nums: List[int], left: int, right: int, quota: int):
        """check if nums[left] + nums[right] < quota = target - basis"""
        while left < right:
            if (nums[left] + nums[right] < quota):
                self.result += (right - left)
                left += 1
            else: # nums[left] + nums[right] >= quota
                right -= 1
```
#### Remark:
- Unlike [Lint57](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/Lintcode_57_3Sum.md), need to return duplicated counts.
- Hesitant about the relationship:
  ```
  basis + left + right < target
  => two_sum < target - basis = quota
  => two_sum < quota
  ```
- Again, as in [Lint609](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/Lintcode_609_Two-Sum-Less-than-or-equal-to-target.md), forgot to increment count by `right-left`, not 1. 
  
#### Submission:
```
Runtime: 1547 ms, faster than 24.80% of Python3 online submissions for 3Sum Smaller.
Memory Usage: 13.9 MB, less than 50.39% of Python3 online submissions for 3Sum Smaller.
```
#### Complexity:
- Time: O(nlogn) + O(n^2)
- Space: O(1)
