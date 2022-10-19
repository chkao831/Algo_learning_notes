### Sudoku Solver
https://leetcode.com/problems/sudoku-solver/

<p>
    <img src="https://leetcode.com/problems/sudoku-solver/Figures/37/37_const3.png" width="600" />
</p>
<p>
    <img src="https://leetcode.com/problems/sudoku-solver/Figures/37/37_backtrack2.png" width="600" />
</p>
<p>
    <img src="https://leetcode.com/problems/sudoku-solver/Figures/36/36_boxes_2.png" width="500" />
</p>
                                                     
>
```python
from typing import (
    List, Dict, Set
)

class Solution:

    def __init__(self):
        self.n = 3
        self.N = 9

    def solve_sudoku(self, board: List[List[int]]):
        def to1Dbox(i: int, j: int) -> int:
            sub_i, sub_j = i//3, j//3
            return sub_i * self.n + sub_j
        
        def initRecordSet() -> Dict:
            occupied = {
                "rows": [set() for _ in range(self.N)],
                "cols": [set() for _ in range(self.N)],
                "boxes": [set() for _ in range(self.N)]
            }
            for i in range(self.N):
                for j in range(self.N):
                    if board[i][j]==0: # cell is empty
                        continue
                    occupied['rows'][i].add(board[i][j])
                    occupied['cols'][j].add(board[i][j])
                    occupied['boxes'][to1Dbox(i,j)].add(board[i][j])
            return occupied
        
        def is_valid(entry_val: int, i: int, j: int, occupied: Dict):
            if entry_val in occupied['rows'][i]: return False
            if entry_val in occupied['cols'][j]: return False
            if entry_val in occupied['boxes'][to1Dbox(i, j)]: return False
            return True
        
        def dfs(cell: int, occupied: Dict) -> bool:
            
            if cell == 81:
                return True
            
            i, j = cell//self.N, cell%self.N # 2Dto1D
            # already occupied
            if board[i][j] != 0:
                dfs(cell+1, occupied) # proceed to next cell
            else:
                for entry in range(1, self.N+1):
                    if not is_valid(entry, i, j, occupied):
                        continue
                    board[i][j] = entry
                    occupied['rows'][i].add(entry)
                    occupied['cols'][j].add(entry)
                    occupied['boxes'][to1Dbox(i,j)].add(entry)
                    if dfs(cell+1, occupied):
                        return True
                    # if sudoku is solved, there is no need to backtrack
                    # since the single unique solution is promised
                    # only backtrack if not solved
                    board[i][j] = 0
                    occupied['boxes'][to1Dbox(i,j)].remove(entry)
                    occupied['cols'][j].remove(entry)
                    occupied['rows'][i].remove(entry)
                return False
                   
        occupied = initRecordSet()
        dfs(cell=0, occupied=occupied)

```
#### Remark:
- 
#### Submission:
```
```
#### Complexity:
- Time:
- Space:
