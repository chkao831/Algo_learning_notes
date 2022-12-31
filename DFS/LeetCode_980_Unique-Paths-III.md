### Unique Paths III
https://leetcode.com/problems/unique-paths-iii/description/
>Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

<p>
    <img src="https://assets.leetcode.com/uploads/2021/08/02/lc-unique1.jpg" width="400" />
</p>

```python
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        results = []
        start_x, start_y = 0, 0
        obstacle = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start_x = i
                    start_y = j 
                elif grid[i][j] == -1:
                    obstacle += 1
        self.dfs(grid=grid, path=[(start_x, start_y)], visited=set([(start_x, start_y)]), cur_x=start_x, cur_y=start_y, results=results, obstacle=obstacle)
        return len(results)

    def dfs(self, grid: List[List[int]], path: List[Tuple[int]], visited: Set, cur_x: int, cur_y: int, results: List[Tuple[int]], obstacle: int):

        def _is_valid(x, y, visited):
            if not 0<=x<len(grid) or not 0<=y<len(grid[0]):
                return False
            if (x, y) in visited:
                return False
            if grid[x][y] == -1:
                return False
            return True

        if grid[cur_x][cur_y] == 2:
            if obstacle + len(path) == len(grid)*len(grid[0]):
                results.append(list(path))
            return
        for d in DIR:
            if not _is_valid(cur_x+d[0], cur_y+d[1], visited):
                continue
            path.append((cur_x+d[0], cur_y+d[1]))
            visited.add((cur_x+d[0], cur_y+d[1]))
            self.dfs(grid, path, visited, cur_x+d[0], cur_y+d[1], results, obstacle)
            visited.remove((cur_x+d[0], cur_y+d[1]))
            path.pop()
```
#### Remark:
- 
#### Submission:
```
Runtime
80 ms
Beats
74.11%

Memory
14 MB
Beats
54.63%
```
#### Complexity:
- Time: O(3^N) (3 directions to choose at each cell; 1 direction is where we come from)
- Space: O(N)
