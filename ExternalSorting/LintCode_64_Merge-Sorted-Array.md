### Merge Sorted Array
https://www.lintcode.com/problem/64/
>Given two sorted integer arrays `A` and `B`, merge `B` into `A` as one sorted array.\
>Modify array `A` **in-place** to merge array `B` into the back of array `A`.
>
>**You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B.**

```python
class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        ptr_A, ptr_B = m-1, n-1
        curr_idx = m+n-1
        while ptr_A >= 0 and ptr_B >= 0:
            if A[ptr_A] >= B[ptr_B]:
                A[curr_idx] = A[ptr_A]
                ptr_A -= 1
            else:
                A[curr_idx] = B[ptr_B]
                ptr_B -= 1
            curr_idx -= 1
        while ptr_A >= 0:
            A[curr_idx] = A[ptr_A]
            curr_idx, ptr_A = curr_idx - 1, ptr_A - 1
        while ptr_B >= 0:
            A[curr_idx] = B[ptr_B]
            curr_idx, ptr_B = curr_idx - 1, ptr_B - 1
        return A
```
#### Remark:
- Key: Need to do it in-place. You may assume that A has enough space
  - 不要用慣性思維從小排到大，不然每次插入新東西，都要後面的全部後移
  - **從大的排，塞到A後面 **
#### Submission:
```
1081 ms
time cost
·
8.52 MB
memory cost
·
Your submission beats
29.20 %
Submissions
```
#### Complexity:
- Time: O(m+n)
- Space: O(1)
