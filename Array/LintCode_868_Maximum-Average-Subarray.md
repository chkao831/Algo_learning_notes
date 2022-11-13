## Maximum Average Subarray
https://www.lintcode.com/problem/868/description
>Given an array consisting of `n` integers, find the contiguous subarray of given length `k` that has the maximum average value. You need to output the maximum average value.
### 暴力模擬
```python
from typing import (
    List,
)

class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the maximum average value
    """
    def find_max_average(self, nums: List[int], k: int) -> float:
        cur_max, cur_starting_idx = float('-inf'), 0
        while cur_starting_idx + k <= len(nums):
            cur_avg = 0
            for i in range(cur_starting_idx, cur_starting_idx+k):
                cur_avg += nums[i]
            cur_avg = cur_avg / k
            if cur_avg > cur_max:
                cur_max = cur_avg
            cur_starting_idx += 1
        return cur_max
```
#### Complexity:
- Time: O(nk)
- Space: O(1)

### Prefix Sum 前綴和
```python
```
#### Remark:
- 
#### Submission:
```
```
#### Complexity:
- Time: O(n)
- Space: O(n)

