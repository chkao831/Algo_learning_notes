### Minimum Average Difference
https://leetcode.com/problems/minimum-average-difference/
>Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.
```python
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum, suffix_sum = [0]*(n+1), [0]*(n+1)
        for i in range(1, len(nums)+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
            suffix_sum[~i] = suffix_sum[~i+1] + nums[~i+1]
        left_avg, right_avg = 0, 0
        min_avg, min_idx = float('inf'), 0
        for i in range(0, n):
            left_avg = prefix_sum[i+1] // (i+1)
            right_denom = n-i-1 if n-i-1 != 0 else 1
            right_avg = suffix_sum[i+1] // right_denom
            curr_avg = abs(left_avg - right_avg)
            if curr_avg < min_avg:
                min_avg = curr_avg
                min_idx = i
        return min_idx
```
#### Remark:
- Trick: 
  - 取得`i`對稱位：用`nums[~i]`
  - 注意index:
    ```python
    nums =          [  1,  4,  5,   6,  3]
    prefix_sum = [0,   1,  5, 10,  16, 19]
    suffix_sum = [19, 18, 14,  9,   3,  0]
               start   ^
                                 end    ^
    ```
#### Submission:
```
Runtime: 1269 ms, faster than 81.09% of Python3 online submissions for Minimum Average Difference.
Memory Usage: 30.9 MB, less than 6.82% of Python3 online submissions for Minimum Average Difference.
```
#### Complexity:
- Time: O(n)
- Space: O(n)
