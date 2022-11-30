# Ugly Number II
https://leetcode.com/problems/ugly-number-ii/
>An ugly number is a positive integer whose prime factors are limited to `2`, `3`, and `5`.
>
>Given an integer `n`, **return the nth ugly number**.

## 暴力因式分解
#### Complexity:
- Time: O(N^(3/2))
    - N個數，每個數因式分解是根號N

## Using Heap
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

## Using Pointers*3
```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ptr_2, ptr_3, ptr_5 = 0, 0, 0
        list_ugly = [1]
        for _ in range(n-1):
            last_ugly = list_ugly[-1]
            while 2*list_ugly[ptr_2] <= last_ugly:
                ptr_2 += 1
            while 3*list_ugly[ptr_3] <= last_ugly:
                ptr_3 += 1
            while 5*list_ugly[ptr_5] <= last_ugly:
                ptr_5 += 1
            list_ugly.append(min(2*list_ugly[ptr_2], 3*list_ugly[ptr_3], 5*list_ugly[ptr_5]))
        return list_ugly[-1]
```
#### Remark:
- 注意，是`2*list_ugly[ptr_2]`，不是`2*ptr_2`，因為限於只含有2、3、5因數的數，要從`list_ugly`裡面取。
#### Submission:
```
Runtime: 176 ms, faster than 84.21% of Python3 online submissions for Ugly Number II.
Memory Usage: 13.9 MB, less than 56.02% of Python3 online submissions for Ugly Number II.
```
#### Complexity:
- Time: O(N)
- Space: O(N)
