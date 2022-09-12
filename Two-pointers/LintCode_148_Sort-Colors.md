### Sort Colors
https://www.lintcode.com/problem/148/
>Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
>
>We will use the integers `0, 1,` and `2` to represent the color red, white, and blue respectively.
```python
from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing

    Get [0 | 1&2] partition first (O(n));
    then get [0 | 1 | 2] partition (O(n)). 
    """
    def sort_colors(self, nums: List[int]):
        if not nums or len(nums)<1:
            return []
        partition_start_1= self.partition(nums=nums, left=0, threshold=1)
        partition_start_2 = self.partition(nums=nums, left=partition_start_1, threshold=2)
        return nums
        
    def partition(self, nums: List[int], left: int, threshold: int):
        right = len(nums)-1
        while left <= right:
            while left <= right and nums[left] < threshold:
                left += 1
            while left <= right and nums[right] >= threshold:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left+1, right-1
        return left

```
#### Remark:
- Should do it in-place.
- Partition twice.
#### Submission:
```
101 ms
time cost
·
6.69 MB
memory cost
·
Your submission beats
92.00 %
Submissions
```
#### Complexity:
- Time: O(n)*2 = O(n)
- Space: O(1)
