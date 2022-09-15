### Partition Array II
https://www.lintcode.com/problem/625/description/
>Partition an unsorted integer array into three parts:
>
>The front part < low\
>The middle part >= low & <= high\
>The tail part > high\
>Return any of the possible solutions.
```python
from typing import (
    List,
)

class Solution:
    """
    @param nums: an integer array
    @param low: An integer
    @param high: An integer
    @return: nothing
    """
    def partition2(self, nums: List[int], low: int, high: int):
        if not nums or low > high:
            return
        left_start = self.partition(nums=nums, left=0, k=low)
        self.partition(nums=nums, left=left_start, k=high)

    def partition(self, nums: List[int], left: int, k: int):
        right = len(nums)-1
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left+1, right-1
        return left
        
```
#### Remark:
- Similar to [Lint148(Sort Colors)](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_148_Sort-Colors.md)
#### Submission:
```
Input Data
[4,3,4,1,2,3,1,2]
2
3
Output Data
[1,1,2,2,3,3,4,4]
```
#### Complexity:
- Time: O(n)
- Space: O(1)
