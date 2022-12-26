# Triangle
https://leetcode.com/problems/triangle/description/
>Given a triangle array, return the minimum path sum from top to bottom.
>
>For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

## DFS (Top down)
```python
class Solution:
    def __init__(self):
        self.global_min = sys.maxsize

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def dfs(x: int, y: int, cur_min: int):
            if x == len(triangle):
                if cur_min < self.global_min:
                    self.global_min = cur_min
                return
            dfs(x+1, y, cur_min+triangle[x][y])
            dfs(x+1, y+1, cur_min+triangle[x][y])
        
        dfs(x=0, y=0, cur_min=0)
        return self.global_min
```
#### Submission:
```
TLE
```
#### Complexity:
- Time: O(2^n) (left and right; like binary tree)
- Space: O(logN)


## DFS (Bottom Up)
關鍵：數字三角形左右是有重複計算的部分的，不是分開的二叉樹，所以可以用cache or memo降低時間複雜度 (from 2^N to N^2)

<p>
    <img src="https://leetcode.com/problems/triangle/solutions/1167943/Figures/120/upside_down_triangle_coordinates.png" width="600" />
</p>
                                                      
```python
class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @lru_cache(None)
        def dfs(x: int, y: int):
            if x == len(triangle):
                return 0
            left = dfs(x+1, y)
            right = dfs(x+1, y+1)
            return min(left, right) + triangle[x][y]
        
        return dfs(x=0, y=0)
```
#### Submission:
```
Runtime
84 ms
Beats
73.60%

Memory
17.6 MB
Beats
5.10%
```
#### Complexity:
- Time: O(N^2), with `@lru_cache ()`
- Space: O(N^2) (額外緩存空間）

## Memoization
使用一個哈希表，進行遞歸之前，先去看之前算過沒有。\
Key: 使用hashmap紀錄搜索的中間結果，下次通過同樣的參數訪問時，直接返回保存下來的結果。\
通過局部最優解，找全局最優解。\
記憶化搜索是DP的實現方式之一。
```python
from typing import List, Dict

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle: List[List[int]]):
    
        def dfs(x: int, y: int, memo: Dict):
            if x == len(triangle):
                return 0
                
            if (x, y) in memo:
                return memo[(x, y)]

            left = dfs(x + 1, y, memo)
            right = dfs(x + 1, y + 1, memo)

            memo[(x, y)] = min(left, right) + triangle[x][y]
            return memo[(x, y)]

        return dfs(0, 0, {})
```
#### Submission:
```
Runtime
83 ms
Beats
74.43%

Memory
17 MB
Beats
12.20%
```
#### Complexity:
- Time: O(N^2)
- Space: O(N^2) (額外緩存空間）
