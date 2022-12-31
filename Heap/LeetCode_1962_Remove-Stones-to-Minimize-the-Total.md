### Remove Stones to Minimize the Total
https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/
>You are given a 0-indexed integer array `piles`, where `piles[i]` represents the number of stones in the ith pile, and an integer `k`. You should apply the following operation exactly `k` times:
>
>Choose any `piles[i]` and remove `floor(piles[i] / 2)` stones from it.
>Notice that you can apply the operation on the same pile more than once.
>
>Return the minimum possible total number of stones remaining after applying the `k` operations.
>
>`floor(x)` is the greatest integer that is smaller than or equal to x (i.e., rounds x down).
```python
from heapq import heappush, heappop

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        # O(nlogn)
        for pile in piles:
            heappush(heap, -pile)
        # O(klogn)
        for operation in range(k):
            current_largest = -heappop(heap)
            removing_val = current_largest // 2
            heappush(heap, -(current_largest-removing_val))
        return -sum(heap)
```
#### Remark:
- An array can alternatively be converted to a heap in linear time O(n) using a method like Python's `heapq.heapify()`
```
heap = [-num for num in piles]
heapq.heapify(heap)
```
#### Submission:
```
Runtime
1779 ms
Beats
73.5%

Memory
29 MB
Beats
26.47%
```
#### Complexity:
- Time: O(n + klogn) with heapify
- Space: O(n)
