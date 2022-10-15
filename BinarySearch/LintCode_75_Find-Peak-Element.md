### Find Peak Element
https://www.lintcode.com/problem/75/
>There is an integer array which has the following features:
>
>**The numbers in adjacent positions are different.**\
>`A[0] < A[1] && A[A.length - 2] > A[A.length - 1]`.\
>We define a position P is a peak if:\
>`A[P] > A[P-1] && A[P] > A[P+1]`\
>Find a peak element in this array. Return the index of the peak.

上升區間右側必有峰\
下降區間左側必有峰\
谷的兩邊都有峰

```python
from typing import (
    List,
)

class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, a: List[int]) -> int:
        if not a:
            return -1
        start, end = 0, len(a)-1
        while start + 1 < end:
            mid = (start+end)//2
            if (a[mid-1] < a[mid] and a[mid] > a[mid+1]):
                return mid
            if a[mid-1] < a[mid]: # but a[mid] < a[mid+1]
                start = mid # go up
            elif a[mid-1] > a[mid]: # a[mid] < or > a[mid+1]
                end = mid
        return max(a[start], a[end])
```
#### Remark:
- 每次取中間元素，如果大於左右，則這就是peek。
  否則取大的一邊，兩個都大，可以隨便取一邊。最終會找到peek。
- 正確性證明：
  - 1. A[0] < A[1] && A[n-2] > A[n-1] 所以一定存在一個peek元素。
  - 2. 二分時，選擇大的一邊, 則留下的部分仍然滿足1 的條件，即最兩邊的元素都小於相鄰的元素。所以仍然必然存在peek。
  - 3. 二分至區間足夠小，長度為3, 則中間元素就是peek。
- 如果題目要求找到 **所有** peak, **是O(n)** 級別
    - 試想 [1, 2, 1, 2, 1, 2, ...], O(n/2) = O(n) 
#### Submission:
```
102 ms
time cost
·
10.27 MB
memory cost
·
Your submission beats
56.40 %
Submissions
```
#### Complexity:
- Time: O(logn)
- Space: O(1)
