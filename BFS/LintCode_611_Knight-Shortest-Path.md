## Knight Shortest Path
https://www.lintcode.com/problem/611/
>Given a knight in a chessboard (a binary matrix with `0` as empty and `1` as barrier) with a source position, find the shortest path to a destination position, return the length of the route.\
>Return `-1` if destination cannot be reached.

<p>
    <img src="../images/611_Knight.jpg" width="500" />
</p>


### 單向BFS

```python
from typing import (
    List,
)
from lintcode import (
    Point,
)

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""

DIRECTIONS = [(1, -2), (2, -1), (2, 1), (1, 2), 
              (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

class Solution:
    
    def __init__(self):
        self.dict_distance = {}

    def shortest_path(self, grid: List[List[bool]], source: Point, destination: Point) -> int:
        """
        @param grid: a chessboard included 0 (false) and 1 (true)
        @param source: a point
        @param destination: a point
        @return: the shortest path 
        """

        def is_valid(x: int, y: int) -> bool:
            if not (0<=x<len(grid) and 0<=y<len(grid[0])):
                return False
            if (x, y) in self.dict_distance:
                return False
            if grid[x][y] == 1:
                return False
            return True

        if not grid or not grid[0]:
            return -1
        queue = collections.deque([(source.x, source.y)])
        self.dict_distance = {(source.x, source.y): 0}
        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return self.dict_distance[(x, y)]
            for d in DIRECTIONS:
                new_x = x + d[0]
                new_y = y + d[1]
                if not is_valid(new_x, new_y):
                    continue
                queue.append((new_x, new_y))
                self.dict_distance[(new_x, new_y)] = self.dict_distance[(x, y)] + 1
        return -1
```
#### Remark:
- `while queue:`, not `if queue:`
#### Submission:
```
774 ms
time cost
·
13.67 MB
memory cost
·
Your submission beats
32.40 %
Submissions
```
#### Complexity:
- Time: O(m*n)
- Space: O(m*n)

### 雙向BFS [原理](https://github.com/chkao831/Algo_learning_notes/tree/main/BFS)

```python
from typing import (
    List, Deque
)
from lintcode import (
    Point,
)

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""

DIRECTIONS = [(1, -2), (2, -1), (2, 1), (1, 2), 
              (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

class Solution:
    
    def __init__(self):
        self.distance = 0

    def shortest_path(self, grid: List[List[bool]], source: Point, destination: Point) -> int:
        """
        @param grid: a chessboard included 0 (false) and 1 (true)
        @param source: a point
        @param destination: a point
        @return: the shortest path 
        """

        def is_valid(x: int, y: int, set_visited: set) -> bool:
            if not (0<=x<len(grid) and 0<=y<len(grid[0])):
                return False
            if (x, y) in set_visited:
                return False
            if grid[x][y] == 1:
                return False
            return True

        def expand_queue(q: Deque, s: set, opp_set: set) -> bool:
            self.distance += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for d in DIRECTIONS:
                    new_x = x + d[0]
                    new_y = y + d[1]
                    if not is_valid(new_x, new_y, s):
                        continue
                    if (new_x, new_y) in opp_set:
                        return True
                    q.append((new_x, new_y))
                    s.add((new_x, new_y))
            return False

        if not grid or not grid[0]:
            return -1
        if (source.x, source.y) == (destination.x, destination.y):
            return 0
        # if grid[destination.x][destination.y] == 1: return -1 # destination is barrier

        forward_queue = collections.deque([(source.x, source.y)])
        backward_queue = collections.deque([(destination.x, destination.y)])
        forward_set = set((source.x, source.y))
        backward_set = set((destination.x, destination.y))

        while forward_queue and backward_queue:
            if expand_queue(q=forward_queue, s=forward_set, opp_set=backward_set):
                return self.distance
            if expand_queue(q=backward_queue, s=backward_set, opp_set=forward_set):
                return self.distance
        return -1
```
#### Remark:
- 注意：是while forward_queue和backward_queue都非空
- 注意：拓展下一層的點不能`while queue:`, 要是`for _ in range(len(queue)):`
#### Submission:
```
752 ms
time cost
·
13.80 MB
memory cost
·
Your submission beats
43.40 %
Submissions
```
#### Complexity:
- Time: O((mn)^(1/2))
- Space: O((mn)^(1/2))
