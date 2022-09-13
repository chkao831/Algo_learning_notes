### Median
https://www.lintcode.com/problem/80/description
>Given a unsorted array with integers, find the median of it.\
>If there are even numbers in the array, return the N/2-th number after sorted.
```python
from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums: List[int]) -> int:
        if not nums: 
            return None
        return self.QuickSelect(nums=nums, start=0, end=len(nums)-1, k=(len(nums)-1)//2)

    def QuickSelect(self, nums: List[int], start: int, end: int, k: int):
        # base
        if start==end:
            return nums[k]
        # recursive
        left, right = start, end
        pivot = nums[(start+end)//2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
        if k <= right:
            self.QuickSelect(nums=nums, start=start, end=right, k=k)
        if k >= left:
            self.QuickSelect(nums=nums, start=left, end=end, k=k)
        return nums[k]

```
#### Remark:
- Mistake: `nums[left] < pivot` and  `nums[right] > pivot`, not `left < pivot` or  `right > pivot`
- `k=(len(nums)-1)//2`, not `k=(len(nums))//2`
#### Submission:
```
102 ms
time cost
·
6.28 MB
memory cost
·
Your submission beats
38.80 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(1)
