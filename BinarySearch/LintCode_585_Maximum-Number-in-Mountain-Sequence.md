### Maximum Number in Mountain Sequence
https://www.lintcode.com/problem/585/
>Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top(Maximum).

<img src="../images/585_Mountain.jpg" width="600px" />

```python
from typing import (
    List,
)

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountain_sequence(self, nums: List[int]) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = (start+end)//2
            if nums[mid] < nums[mid+1]:
                start = mid
            else: #nums[mid] > nums[mid+1], no equal case due to strictly increasing/decreasing
                end = mid
        return max(nums[start], nums[end])

```
#### Remark:
```
1 2 3 4 5 4 3 2 1
O O O O X X X X X
condition: nums[i] > nums[i+1], when found, give it X (end)
```
#### Submission:
```
204 ms
time cost
·
13.85 MB
memory cost
·
Your submission beats
7.60 %
Submissions
```
#### Complexity:
- Time: O(logn)
- Space: O(1)
