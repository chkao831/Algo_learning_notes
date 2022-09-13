### Median of two Sorted Arrays
https://www.lintcode.com/problem/65/description
>There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.The overall run time complexity should be O(log(m+n)).

```python
from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @param b: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def find_median_sorted_arrays(self, a: List[int], b: List[int]) -> float:
        c = len(a) + len(b)
        if c % 2 == 1:
            k = (c//2) + 1
            return self.findkth(a, b, k)
        else:
            k1 = (c//2)
            k2 = (c//2) + 1
            n1 = self.findkth(a, b, k1)
            n2 = self.findkth(a, b, k2)
            return (n1 + n2)/2.0
    
    def findkth(self, a: List[int], b: List[int], k: int) -> int:
        if len(a) == 0:
            return b[k-1]
        if len(b) == 0:
            return a[k-1]
        
        start = min(a[0], b[0])
        end = max(a[len(a)-1], b[len(b)-1])

        # start and end never touch
        while start + 1 < end:
            mid = (start + end)//2
            # <= | >
            c1 = self.countSmaller(a, mid)
            c2 = self.countSmaller(b, mid)
            # c1 + c2 is counts for val >= mid
            if c1 + c2 >= k: 
                end = mid # left shift
            else:
                start = mid # right shift
        # start and end off by 1
        if self.countSmaller(a, start) + self.countSmaller(b, start) >= k:
            return start
        else:
            return end

    def countSmaller(self, arr: List[int], mid_val: int) -> int:
        left, right = 0, len(arr)-1
        while left + 1 < right:
            mid = (left + right) //2
            if arr[mid] <= mid_val:
                left = mid
            else: # arr[mid] > mid_val
                right = mid
        # return the position at which its value is bigger than mid_val
        if arr[left] > mid_val:
            return left
        if arr[right] > mid_val:
            return right
        return len(arr)
```
#### Remark:
- 
#### Submission:
```
102 ms
time cost
·
6.20 MB
memory cost
·
Your submission beats
21.20 %
Submissions
```
#### Complexity:
- Time: O((range)log(m+n)) 
  - 每一輪循環可以將查找範圍減少一半
  - `range = max(a[len(a)-1], b[len(b)-1]) - min(a[0], b[0])`
- Space: O(1)
