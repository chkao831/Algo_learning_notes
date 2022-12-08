### Merge Two Sorted Arrays
https://www.lintcode.com/problem/6/
>Merge two given sorted ascending integer array A and B into a new sorted integer array.

```python
from typing import (
    List,
)

class Solution:
    """
    @param a: sorted integer array A
    @param b: sorted integer array B
    @return: A new sorted integer array
    """
    def merge_sorted_array(self, a: List[int], b: List[int]) -> List[int]:
        a_ptr, b_ptr = 0, 0
        arr_out = []
        while a_ptr < len(a) and b_ptr < len(b):
            if a[a_ptr] <= b[b_ptr]:
                arr_out.append(a[a_ptr])
                a_ptr += 1
            else:
                arr_out.append(b[b_ptr])
                b_ptr += 1
        while a_ptr < len(a):
            arr_out.append(a[a_ptr])
            a_ptr += 1
        while b_ptr < len(b):
            arr_out.append(b[b_ptr])
            b_ptr += 1
        return arr_out
```
#### Remark:
- 
#### Submission:
```
122 ms
time cost
·
8.53 MB
memory cost
·
Your submission beats
53.20 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(1) (no extra space)
