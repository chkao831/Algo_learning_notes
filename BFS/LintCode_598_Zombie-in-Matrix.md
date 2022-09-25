### Zombie in Matrix
https://www.lintcode.com/problem/598/
>Give a two-dimensional grid, each grid has a value, 2 for wall, 1 for zombie, 0 for human (numbers 0, 1, 2).Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall. How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.
```python
from typing import (
    List,
)

DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]

class Solution:
    
    def __init__(self):
        self.dict_distance = {}

    def zombie(self, grid: List[List[int]]) -> int:
        """
        @param grid: a 2D integer grid
        @return: an integer
        """

        def is_valid(x: int, y: int) -> bool:
            if not (0<=x<len(grid) and 0<=y<len(grid[0])):
                return False
            if (x, y) in self.dict_distance:
                return False
            if grid[x][y] == 1 or grid[x][y] == 2:
                return False
            return True

        if not grid or not grid[0]:
            return -1
        
        sum_walls, sum_zombies = 0, 0
        queue = collections.deque([])

        for i in range(len(grid)): # O(mn) time
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    sum_walls += 1
                elif grid[i][j] == 1:
                    queue.append((i, j))
                    self.dict_distance[(i, j)] = 0
                    sum_zombies += 1

        max_distance = 0
        while queue: # O(mn) time; O(mn) space
            x, y = queue.popleft()
            for d in DIRECTIONS:
                new_x = x + d[0]
                new_y = y + d[1]
                if not is_valid(new_x, new_y):
                    continue
                # by here, verified that grid[new_x][new_y] is new human
                grid[new_x][new_y] = 1
                queue.append((new_x, new_y))
                self.dict_distance[(new_x, new_y)] = self.dict_distance[(x, y)]+1
                max_distance = max(max_distance, self.dict_distance[(new_x, new_y)])
                sum_zombies += 1
        if sum_zombies + sum_walls == len(grid) * len(grid[0]):
            return max_distance
        else:
            return -1
```
#### Remark:
- 
#### Submission:
```
121 ms
time cost
·
6.24 MB
memory cost
·
Your submission beats
41.40 %
Submissions
```
#### Complexity:
- Time: O(m*n)
- Space: O(m*n)
