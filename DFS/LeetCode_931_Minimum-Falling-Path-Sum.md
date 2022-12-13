### Minimum Falling Path Sum
https://leetcode.com/problems/minimum-falling-path-sum/description/
>Given an `n` x `n` array of integers `matrix`, return the minimum sum of any falling path through `matrix`.

<p>
    <img src="https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg" width="400" />
</p>

```python
DIR = [(1, -1), (1, 0), (1, 1)]

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix) 

        def _isValid(i: int, j: int) -> bool:
            nonlocal n
            if not 0<=i<n or not 0<=j<n:
                return False
            return True

        @lru_cache(None)
        def _dfs(i: int, j: int) -> int:
            nonlocal n, matrix
            # base
            if not _isValid(i, j):
                return sys.maxsize
            if i == n-1:
                return matrix[i][j]
            # recursive
            left = _dfs(i+DIR[0][0], j+DIR[0][1])
            mid = _dfs(i+DIR[1][0], j+DIR[1][1])
            right = _dfs(i+DIR[2][0], j+DIR[2][1])
            return min(left, mid, right) + matrix[i][j]

        cur_min = sys.maxsize
        for starting_position in range(n):
            cur_min = min(cur_min, _dfs(i=0, j=starting_position))
        return cur_min
```
#### Remark:
- Without `@lru_cache(None)`, would get TLE.
- base case: reaching the end row or taking an invalid step.
#### Submission:
```
Runtime
169 ms
Beats
82.95%

Memory
22.9 MB
Beats
5.72%
```
#### Complexity:
- Time: O(N*3^N) - 對於每個起點，啟三叉樹
- Space: O(N) - depth of the recursive stack
