### Range Addition II
https://www.lintcode.com/problem/1144/description
>Given an m * n matrix M initialized with all 0's and several update operations.
>
>Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.
>
>You need to count and return the number of maximum integers in the matrix after performing all the operations.

#### Intuitively, O(m*n) time and O(m*n) space
```python
from typing import (
    List,
)

class Solution:
    """
    @param m: an integer
    @param n: an integer
    @param ops: List[List[int]]
    @return: return an integer
    """
    def max_count(self, m: int, n: int, ops: List[List[int]]) -> int:
        matrix = [ [ 0 for i in range(m) ] for j in range(n) ] # O(mn) time, O(mn) space
        for op in ops: # O(mn) time
            self.operation(matrix, op)
        return self.count_max(matrix) # O(mn) time

    def operation(self, matrix: List[List[int]], op: List[int]):
        for i in range(op[0]):
            for j in range(op[1]):
                matrix[i][j] += 1

    def count_max(self, matrix):
        num = -1
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] > num:
                    num = matrix[i][j]
                    count = 1
                elif matrix[i][j] == num:
                    count += 1
        return count
```
#### Could reduce to O(1) time and O(1) space (len(ops) is fixed=2)
對於任意兩個操作[op11, op12], [op21, op22], 其所能涵蓋的面積的交集為[min(op11, op21), max(op12, op22)]
```python
from typing import (
    List,
)

class Solution:
    """
    @param m: an integer
    @param n: an integer
    @param ops: List[List[int]]
    @return: return an integer
    """

    def maxCount(self, m, n, ops):
        res_m, res_n = m, n
        for op in ops:
            res_m, res_n = min(res_m, op[0]), min(res_n, op[1])
        return res_m * res_n
```
#### Remark:
- 
#### Submission:
```
102 ms
time cost
·
7.00 MB
memory cost
·
Your submission beats
21.32 %
Submissions
```
#### Complexity:
- Time: O(2*2) = O(4) => O(1)
- Space: O(1)
