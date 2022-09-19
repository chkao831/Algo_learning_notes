### Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/
>Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
>
> - Integers in each row are sorted in ascending from left to right.
> - Integers in each column are sorted in ascending from top to bottom.

<img src="../images/240_Matrix-Search.jpg" width="500px" />

```python
```
#### Remark:
- 因為要算次數 理論的時間複雜度不低於O(n) 只能一個個找到 不太能批量去找
```
想法一：每一row Binary Search
1 3 5 7
2 4 7 8
3 5 9 10
每排logn -> 總共nlogn -> 太大 （只用到了row有排序的信息）

想法二：象限排除
target = 3, matrx[mid]=4
排除右下角9 10
1 3 | 5 7
2 4 | 7 8
--------
3 5 | 9 10

n -> 3/4 n with an operation
T(n) = 3T(n/2) + O(1) [邊長變一半] -> T(n) = O(n)
```
以上想法都不太可行
#### Submission:
```
```
#### Complexity:
- Time: O(m+n) = O(max(m, n)) as its worst case, since each row (or column) might have something to be visited
- Space: O(1)
