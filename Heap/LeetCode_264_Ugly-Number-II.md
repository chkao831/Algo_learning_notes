### Ugly Number II
https://leetcode.com/problems/ugly-number-ii/
>An ugly number is a positive integer whose prime factors are limited to `2`, `3`, and `5`.
>
>Given an integer `n`, **return the nth ugly number**.

```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap, set_visited = [1], set([1])
        for i in range(n):
            num = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                if factor*num not in set_visited:
                    heapq.heappush(heap, factor*num)
                    set_visited.add(factor*num)
        return num
```
#### Remark:
- `heapq` is a minHeap; for maxHeap, negate all numbers. 
#### Submission:
```
Runtime: 194 ms, faster than 80.74% of Python3 online submissions for Ugly Number II.
Memory Usage: 14.1 MB, less than 21.64% of Python3 online submissions for Ugly Number II.
```
#### Complexity:
- Time: O(NlogN)
  - `for i in range(n)` -> O(N)
  - `heapq.heappop()` -> O(logN) 
- Space: O(N)
