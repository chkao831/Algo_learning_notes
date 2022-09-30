## Knight Shortest Path II
https://www.lintcode.com/problem/630/
>Given a knight in a chessboard n * m (a binary matrix with `0` as empty and `1` as barrier). the knight initialze position is (0, 0) and he wants to reach position (n - 1, m - 1), Knight can only be from left to right. Find the shortest path to the destination position, return the length of the route. 
>Return -1 if knight can not reached.

### 單向BFS

```python
from typing import (
    List,
)

DIRECTIONS = [(1, 2), (-1, 2), (2, 1), (-2, 1)]

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    
    def __init__(self):
        self.dict_distance = {}

    def shortest_path2(self, grid: List[List[bool]]) -> int:
        """
        @param grid: a chessboard included 0 and 1
        @return: the shortest path
        """

        def is_valid(i: int, j: int) -> bool:
            if not (0<=i<len(grid) and 0<=j<len(grid[0])):
                return False
            if (i, j) in self.dict_distance:
                return False
            if grid[i][j] == 1:
                return False
            return True

        source = Point(x=0, y=0)
        destination = Point(x=len(grid)-1, y=len(grid[0])-1)
        if not grid or not grid[0] or not grid[destination.x][destination.y]==0:
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
- 
#### Submission:
```
506 ms
time cost
·
8.41 MB
memory cost
·
Your submission beats
52.00 %
Submissions
```
#### Complexity:
- Time: O(m*n)
- Space: O(m*n)

### 雙向BFS [原理](https://github.com/chkao831/Algo_learning_notes/tree/main/BFS#雙向bfs-bidirectional-bfs)

```python
from typing import (
    List, Deque
)

FORWARD_DIRECTIONS = [(1, 2), (-1, 2), (2, 1), (-2, 1)]
BACKWARD_DIRECTIONS = [(-1, -2), (1, -2), (-2, -1), (2, -1)]

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    
    def __init__(self):
        self.distance = 0

    def shortest_path2(self, grid: List[List[bool]]) -> int:
        """
        @param grid: a chessboard included 0 and 1
        @return: the shortest path
        """

        def is_valid(i: int, j: int, set_visited: set) -> bool:
            if not (0<=i<len(grid) and 0<=j<len(grid[0])):
                return False
            if (i, j) in set_visited:
                return False
            if grid[i][j] == 1:
                return False
            return True

        def expand_queue(q: Deque, s: set, opp_set: set, direc: List) -> bool:
            self.distance += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for d in direc:
                    new_x = x + d[0]
                    new_y = y + d[1]
                    if not is_valid(new_x, new_y, s):
                        continue
                    if (new_x, new_y) in opp_set:
                        return True
                    q.append((new_x, new_y))
                    s.add((new_x, new_y))
            return False
        
        source = Point(x=0, y=0)
        destination = Point(x=len(grid)-1, y=len(grid[0])-1)
        if not grid or not grid[0] or not grid[destination.x][destination.y]==0:
            return -1

        forward_queue = collections.deque([(source.x, source.y)])
        backward_queue = collections.deque([(destination.x, destination.y)])
        forward_set = set([(source.x, source.y)])
        backward_set = set([(destination.x, destination.y)])

        while forward_queue and backward_queue:
            if expand_queue(q=forward_queue, s=forward_set, opp_set=backward_set, direc=FORWARD_DIRECTIONS):
                return self.distance
            if expand_queue(q=backward_queue, s=backward_set, opp_set=forward_set, direc=BACKWARD_DIRECTIONS):
                return self.distance
        return -1
```
#### Remark:
- 注意：是while forward_queue和backward_queue都非空
- 注意：拓展下一層的點不能`while queue:`, 要是`for _ in range(len(queue)):`
- 雙向的方向變了！因為此題forward馬只能向右走，backward時正負號全部要反過來
#### Submission:
```
550 ms
time cost
·
9.61 MB
memory cost
·
Your submission beats
49.60 %
Submissions
```
#### Complexity:
- Time: O((mn)^(1/2))
- Space: O((mn)^(1/2))
