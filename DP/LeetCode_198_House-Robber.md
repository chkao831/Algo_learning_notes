### House Robber
https://leetcode.com/problems/house-robber/description/
>Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police (if two adjacent houses were broken into on the same night).
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        sum = [0]*len(nums)
        sum[0] = nums[0]
        sum[1] = max(nums[0], nums[1])
        for i in range(2, n):
            sum[i] = max(sum[i-2]+nums[i], sum[i-1])
        return sum[n-1]
```
#### Remark:

<p>
    <img src="https://leetcode.com/problems/house-robber/solutions/1113644/Figures/198/img4.png" width="800" />
</p>
                                                      
- `robFrom(i)=max(robFrom(i+1),robFrom(i+2)+nums(i))`
#### Submission:
```
Runtime
34 ms
Beats
90.89%

Memory
13.8 MB
Beats
97.62%
```
#### Complexity:
- Time: O(N) - use the pre-calculated values of our dynamic programming table for calculating the current value in the table which is a constant time operation.
- Space: O(N)
