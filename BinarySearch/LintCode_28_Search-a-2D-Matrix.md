### Search a 2D Matrix
https://www.lintcode.com/problem/28/description
>Write an efficient algorithm that searches for a target value in an m x n matrix.
```python
from typing import (
    List,
)

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1
        while left + 1 < right:
            mid = (left+right)//2
            entry_i, entry_j = mid // n, mid % n
            if matrix[entry_i][entry_j] == target:
                return True
            elif matrix[entry_i][entry_j] < target:
                left = mid
            else:
                right = mid
                
        if matrix[right // n][right % n] == target:
            return True
        if matrix[left // n][left % n] == target:
            return True
        return False
```
#### Remark:
- key: [2Dto1D conversion](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LeetCode_74_Search-a-2D-Matrix.md)
#### Submission:
```
387 ms
time cost
·
6.79 MB
memory cost
·
Your submission beats
68.00 %
Submissions
```
#### Complexity:
- Time: O(logN)
- Space: O(1)
