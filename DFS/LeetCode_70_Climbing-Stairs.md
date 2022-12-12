## Climbing Stairs
https://leetcode.com/problems/climbing-stairs/description/
>You are climbing a staircase. It takes `n` steps to reach the top.
>
>Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



### DFS (Brute Force)
Inspired by [Leet91 - Decode Ways](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_91_Decode-Ways.md)
<p>
    <img src="https://leetcode.com/problems/climbing-stairs/solutions/127722/Figures/70_Climbing_Stairs_rt.jpg" width="600" />
</p>

```python
class Solution:
    
    def climbStairs(self, n: int) -> int:
        
        @lru_cache(None)
        def dfs(steps: int) -> int:
            if steps > n:
                return 0
            if steps == n:
                return 1
            return dfs(steps+1) + dfs(steps+2)

        total_combo = dfs(steps=0)
        return total_combo
```
#### Remark:
- without `@lru_cache(None)`, yields Time Limit Exceeded.

#### Submission:
```
Runtime
26 ms
Beats
97.90%

Memory
13.9 MB
Beats
58.8%
```
#### Complexity:
- Time: O(2^n) without LRU cache; O(n) with LRU cache.
- Space: O(n) (max depth of the tree)

### DP

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0]*(n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1, 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
```

#### Remark:
- Fibonacci

#### Submission:
```
Runtime
62 ms
Beats
20.89%

Memory
13.9 MB
Beats
58.8%
```
#### Complexity:
- Time: O(n)
- Space: O(n)
