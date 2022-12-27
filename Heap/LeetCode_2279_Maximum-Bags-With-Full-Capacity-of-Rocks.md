### Maximum Bags With Full Capacity of Rocks
https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/description/
>You have `n` bags numbered from `0` to `n - 1`. You are given two 0-indexed integer arrays `capacity` and `rocks`. The `ith` bag can hold a maximum of `capacity[i]` rocks and currently contains `rocks[i]` rocks. You are also given an integer `additionalRocks`, the number of additional rocks you can place in any of the bags.
>
>Return the maximum number of bags that could have full capacity after placing the additional rocks in some bags.
```python
from heapq import heappush, heappop

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        heap = []
        count, remainingRocks = 0, additionalRocks
        # O(N)
        for i in range(len(capacity)):
            diff = capacity[i] - rocks[i]
            if diff == 0:
                count += 1
            else:
                heappush(heap, diff)
        # O(NlogN) in worst case
        while heap:
            to_be_filled = heappop(heap)
            if to_be_filled <= remainingRocks:
                count += 1
                remainingRocks -= to_be_filled
            else:
                break
        return count
```
#### Remark:
- Alternatively, can use `remaining_capacity = [cap - rock for cap, rock in zip(capacity, rocks)]` and sort in place.
#### Submission:
```
Runtime
1019 ms
Beats
76.32%

Memory
22 MB
Beats
87.83%
```
#### Complexity:
- Time: O(NlogN)
- Space: O(N)
