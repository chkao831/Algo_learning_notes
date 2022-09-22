### Number of Islands
https://www.lintcode.com/problem/433/description
>Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.
>
>Find the number of islands.
```python
from typing import (
    List,
)

DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)] # up, down, left, right

class Solution:

    def __init__(self):
        self.grid = []
        self.set_visited = set()

    def num_islands(self, grid: List[List[bool]]) -> int:
        """
        @param grid: a boolean 2D matrix
        @return: an integer
        """

        def bfs(x: int, y: int):
            queue = collections.deque([(x, y)])
            self.set_visited.add((x, y))
            while queue:
                (x, y) = queue.popleft()
                for d in DIRECTIONS:
                    next_x = x + d[0]
                    next_y = y + d[1]
                    if not cell_is_valid(next_x, next_y):
                        continue
                    queue.append((next_x, next_y))
                    self.set_visited.add((next_x, next_y))

        def cell_is_valid(x: int, y: int) -> bool:
            if not (0<=x<len(grid) and 0<=y<len(grid[0])):
                return False
            if ((x,y) in self.set_visited):
                return False
            if grid[x][y] == 0:
                return False
            return True

        if not grid or not grid[0]:
            return 0
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and not ((i, j) in self.set_visited):
                    bfs(x=i, y=j)
                    island += 1
        return island
```
#### Remark:
- Mistakes:
  - forgot to `queue.popleft()`
  - `if grid[i][j] and not ((i, j) in self.set_visited)` 
  - `if grid[x][y] == 0: return False`
  - `if not (0<=x<len(grid) and 0<=y<len(grid[0])): return False`
#### Submission:
```
284 ms
time cost
·
10.54 MB
memory cost
·
Your submission beats
50.00 %
Submissions
```
#### Complexity:
- Time: O(m*n)
- Space: O(m*n)
