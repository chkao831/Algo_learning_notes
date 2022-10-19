### Sudoku Solver
https://www.lintcode.com/problem/802/description

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
from typing import Dict, List

class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """
    def solveSudoku(self, board: List):
        used = self.initial_used(board)
        self.dfs(board, 0, used)
        
    def to1Dbox(self, i: int, j: int) -> int:
        sub_i, sub_j = i//3, j//3
        return sub_i * 3 + sub_j

    def initial_used(self, board: List) -> Dict:
        used = {
            'row': [set() for _ in range(9)],
            'col': [set() for _ in range(9)],
            'box': [set() for _ in range(9)],
        }
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    continue
                used['row'][i].add(board[i][j])
                used['col'][j].add(board[i][j])
                used['box'][self.to1Dbox(i,j)].add(board[i][j])
                
        return used

    def is_valid(self, i: int, j: int, val: int, used: Dict):
        if val in used['row'][i]:
            return False
        if val in used['col'][j]:
            return False
        if val in used['box'][i // 3 * 3 + j // 3]:
            return False
        return True

    def dfs(self, board: List, index: int, used: Dict) -> bool:
        if index == 81:
            return True
            
        i, j = index // 9, index % 9
        if board[i][j] != 0:
            return self.dfs(board, index + 1, used)
        
        for val in range(1, 10):
            if not self.is_valid(i, j, val, used):
                continue
            
            board[i][j] = val
            used['row'][i].add(val)
            used['col'][j].add(val)
            used['box'][self.to1Dbox(i,j)].add(val)
            
            if self.dfs(board, index + 1, used):
                return True
            
            # if sudoku is solved, there is no need to backtrack
            # since the single unique solution is promised
            # Do backtracking only if not solved
            used['box'][self.to1Dbox(i,j)].remove(val)
            used['col'][j].remove(val)
            used['row'][i].remove(val)
            board[i][j] = 0
        
        return False

```
#### Remark:
- Matrix [1D->2D and 2D->1D tricks](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LeetCode_74_Search-a-2D-Matrix.md)
#### Submission:
```
268 ms
time cost
·
6.00 MB
memory cost
·
Your submission beats
68.20 %
Submissions
```
#### Complexity:
- Time: O(9!)^9
- Space: O(81)
