### Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
>Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
>
>- Integers in each row are sorted from left to right.
>- The first integer of each row is greater than the last integer of the previous row.

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        """ Supplemental Tips
        def to1D(i: int, j: int) -> int:
            n = len(matrix[0]) # total columns
            index = i*n+j
            return index
        """
        
        def to2D(entry: int) -> int:
            n = len(matrix[0]) # total columns
            i = entry//n
            j = entry%n
            return matrix[i][j]

        total_entry = len(matrix)*len(matrix[0])
        start, end = 0, total_entry-1
        while start+1 < end:
            mid = (start+end)//2
            if to2D(mid) >= target:
                end = mid
            else: # to2D(mid) < target:
                start = mid

        if to2D(start) == target: return True
        if to2D(end) == target: return True
        
        return False
```
#### Remark:
1D to 2D:
```
       m
    0 1 2 3
n   4 5 6 7 
    8 9 10 11 
    ^ ^
 (2,0)(2,1) where 2 is obtained by 8//3 and 9//3; 0 and 1 obtained by 8%3 and 9%3
```
2D to 1D:
```
for entry (i, j) in a (n, m) matrix
1D index is i*m+j
```
#### Submission:
```
Runtime: 99 ms, faster than 9.63% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 14.4 MB, less than 43.14% of Python3 online submissions for Search a 2D Matrix.
```
#### Complexity:
- Time: O(logn)
- Space: O(1)
