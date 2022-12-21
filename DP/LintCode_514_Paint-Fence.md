### Paint Fence
https://www.lintcode.com/problem/514/
>There is a fence with `n` posts, each post can be painted with one of the `k` colors.\
>You have to paint all the posts such that no more than two adjacent fence posts have the same color.\
>Return the total number of ways you can paint the fence.
```python
class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def num_ways(self, n: int, k: int) -> int:
        #采用动态规划的思想。
        #dp[i]=(k-1)×(dp[i-1]+dp[i-2]) 
        #dp[i-1]×(k-1)代表当前格子的颜色和前一个不同的方案 
        #dp[i-2]×(k-1)代表当前格子的颜色和前一个相同的方案
        #当前和上一个不同色，已知n-1时有dp[n - 1]种可能，然后n选和n-1不一样的k-1种新颜色，
        #当前和上一个同色的时候, 已知n-2有dp[n - 2]种可能，然后n-1 n-2都选一样的颜色，但需要和n-2不同，有k-1种选择
        dp = [0, k, k * k]
        if n <= 2:
            return dp[n]
        if k == 1 and n >= 3:
            return 0
        for i in range(2, n):
            dp.append((k - 1) * (dp[-1] + dp[-2]))

        return dp[-1]
```
#### Remark:
- 
#### Submission:
```
81 ms
time cost
·
5.99 MB
memory cost
·
Your submission beats
99.60 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(n)
