### Find K Closest Elements
https://www.lintcode.com/problem/460/
> Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. 
> **Otherwise, sorted in ascending order by number if the difference is same.**
```python
from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def k_closest_numbers(self, a: List[int], target: int, k: int) -> List[int]:
        
        def binary_search() -> int:
            start, end = 0, len(a) - 1
            while start + 1 < end:
                mid = (start + end)//2
                if a[mid] < target:
                    start = mid
                else:
                    end = mid
            if a[start] >= target: return start
            if a[end] >= target: return end
            return len(a) # not found
        
        def left_closer(right: int, left: int) -> bool:
            # edge case
            if left < 0: # must be right closer
                return False
            if right >= len(a): # must be left closer
                return True
            return True if target - a[left] <= a[right] - target else False

        out = []
        right = binary_search()
        left = right - 1
        for _ in range(k):
            if left_closer(right, left):
                out.append(a[left])
                left -= 1
            else:
                out.append(a[right])
                right += 1
        return out
```
#### Remark:
- A mistake:
  - `return True if target - a[left] <= a[right] - target else False`, not `<`, because **sorted in ascending order by number if the difference is same**, indicating that left always first. 
#### Submission:
```
122 ms
time cost
·
8.39 MB
memory cost
·
Your submission beats
65.80 %
Submissions
```
#### Complexity:
- Time: O(logn) + O(k)
- Space: O(1)
