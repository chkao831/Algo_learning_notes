### Last Position of Target
https://www.lintcode.com/problem/458/
>Find the last position of a target number in a sorted array. Return -1 if target does not exist.
```python
from typing import (
    List,
)

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def last_position(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = (start+end)//2
            if nums[mid] == target:
                start = mid
            elif nums[mid] < target: # go up
                start = mid
            else: # go down
                end = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1
```
#### Remark:
- Difference from Classical Binary Search (first position):
  - `if nums[mid] == target`, then **go up**
  - in the last judgment, judge `end` first
#### Submission:
```
468 ms
time cost
·
31.89 MB
memory cost
·
Your submission beats
66.00 %
Submissions
```
#### Complexity:
- Time: O(logn)
- Space: O(1)
