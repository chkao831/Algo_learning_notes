### Build Post Office II
https://www.lintcode.com/problem/573/
>Given a 2D grid, each cell is either a `wall 2`, an `house 1` or `empty 0` (the number zero, one, two), find a place to build a post office so that **the sum of the distance from the post office to all the houses is smallest.**\
> Returns the sum of the minimum distances from all houses to the post office.\
> Return `-1` if it is not possible.


- Step 1: 首次遍歷網格，對於每個房子進行bfs，每到一處空地就把那個空地的reachable_house+1，distance加上距離當前房子的距離。
- Step 2: 統計第一步裡面都能到達的空地距離所有房子的最小距離
```python
from typing import (
    List, Set, Dict
)

DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]

class Solution:
    
    def __init__(self):
        self.dist = []
        self.reachable_count = []

    def shortestDistance(self, grid):
        # @param {int[][]} grid a 2D grid
        # @return {int} an integer

        def bfs(i: int, j: int):

            def is_valid(x: int, y: int) -> bool:
                if not (0<=x<len(grid) and 0<=y<len(grid[0])):
                    return False
                if visited[x][y]:
                    return False
                if grid[x][y] == 1 or grid[x][y] == 2:
                    return False
                return True

            visited = [[False for y in range(n)] for x in range(m)]
            visited[i][j] = True
            queue = collections.deque([(i,j,0)])
            
            while queue:
                i, j, level = queue.popleft()
                # update two global variables
                if self.dist[i][j] == sys.maxsize:
                    self.dist[i][j] = 0
                self.dist[i][j] += level
                self.reachable_count[i][j] += 1
                for d in DIRECTIONS:
                    nx, ny = i+d[0], j+d[1]
                    if not is_valid(nx, ny): continue
                    # update two local variables
                    visited[nx][ny] = True
                    queue.append((nx, ny, level+1))

        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        self.dist = [[sys.maxsize for j in range(n)] for i in range(m)]
        self.reachable_count = [[0 for j in range(n)] for i in range(m)]
        
        buildings = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
                    buildings += 1
        min_dist = sys.maxsize
        for i in range(m):
            for j in range(n):
                if self.reachable_count[i][j] == buildings:
                    min_dist = min(self.dist[i][j], min_dist)
        return min_dist if min_dist != sys.maxsize else -1
```
#### Remark:
- `sys.maxsize == 2^63 – 1, i.e. 9223372036854775807`
- 這裡得知第幾層的方式沒有用dictionary來捕捉，而是當作queue的第三個元素
- 注意global & local參數使用
  - global: `self.dist` (2D distance recorder), `self.reachable_count` (2D count recorder)
  - local: `queue`, `visited` (2D boolean visiting recorder) -- 每次bfs都要用新的

#### Submission:
```
1451 ms
time cost
·
12.63 MB
memory cost
·
Your submission beats
16.80 %
Submissions
```
#### Complexity:
- Time: O(HOUSEmn)
- Space: O(mn)
