- return an array of all the **unique** quadruplets `[nums[a], nums[b], nums[c], nums[d]]` 
- You may return the answer **in any order**. 

```python
class Solution:
    """
    [w, x, y, z]
     ^  ^  ^  ^
     b1 b2 l  r where b1=basis_1, b2=basis_2, l=left, r=right
     b1: outer for loop; b2: inner for loop
    """
    def __init__(self):
        self.result = []
        
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        if not nums or len(nums)<4:
            return self.result
        nums.sort() #O(nlogn)
        
        for i in range(0, len(nums)-3): # b1 pointer
            
            if i > 0 and nums[i-1] == nums[i]: continue # skip for b1 pointer duplication
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target: break # smallest still to big
            if nums[i] + nums[len(nums)-3] + nums[len(nums)-2] + nums[len(nums)-1] < target: continue # largest still to small
            
            for j in range(i+1, len(nums)-2): # b2 pointer
                
                if j > (i+1) and nums[j-1] == nums[j]: continue # skip for b2 pointer duplication
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target: break # smallest still to big
                if nums[i] + nums[j] + nums[len(nums)-2] + nums[len(nums)-1] < target: continue # largest still to small
                    
                left, right = j+1, len(nums)-1
                self.twoSumCalc(nums, left, right, nums[i], nums[j], target) # pass in result list append
        return self.result
                
    def twoSumCalc(self, nums: List[int], left: int, right: int, b1: int, b2: int, target: int):
        # b1 + b2 + left + right = target => left + right (two_sum) = target - b1 - b2 = quota
        quota = target - b1 - b2
        while left < right:
            if (nums[left] + nums[right] == quota):
                self.result.append([b1, b2, nums[left], nums[right]])
                left += 1
                right -= 1
                while (left < right and nums[left] == nums[left-1]): left += 1 # skip for left pointer duplication
                while (left < right and nums[right] == nums[right+1]): right -= 1 # skip for right pointer duplication
            elif (nums[left] + nums[right] > quota):
                right -= 1
            else: # (nums[left] + nums[right] < quota)
                left += 1
```
#### Remark:
- Made a mistake on `if j > (i+1) and nums[j-1] == nums[j]: continue` (skip for b2 pointer duplication)
  - originally missed the index constraint and failed the test case 
  ```
  Input
  [2,2,2,2,2]
  8
  Output
  []
  Expected
  [[2,2,2,2]]
  ```
#### Submission:
```
Runtime: 113 ms, faster than 95.78% of Python3 online submissions for 4Sum.
Memory Usage: 14 MB, less than 60.66% of Python3 online submissions for 4Sum.
```
#### Complexity:
- Time: O(nlogn) + O(n^3) = O(n^3)
  - in-place sorting = O(nlogn)
  - Outer_for_loop (O(n)) * Inner_for_loop (O(n)) * Two_sum (O(n)) = O(n^3) 
- Space: O(k) where k=number of solution(s)
