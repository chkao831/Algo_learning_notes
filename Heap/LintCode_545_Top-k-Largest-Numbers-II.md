# Top k Largest Numbers II
https://www.lintcode.com/problem/545/description
>Implement a data structure, provide two interfaces:
>
>`add(number)`. Add a new number in the data structure.
>`topk()`. Return the top `k` largest numbers in this data structure. `k` is given when we create the data structure.

Very Similar to [Lint612 - K Closest Points](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LintCode_612_K-Closest-Points.md)
## Quick Select + Sort Top K = O(n + klogk) topk; O(1) add
```python
from heapq import heappush, heappop

class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.top_k = k
        self.arr = []

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num): # O(1)
        self.arr.append(num)

    """
    @return: Top k element
    """
    def topk(self): # O(n+klogk)

        def _quickSelect(start: int, end: int, k: int):
            if start >= end:
                return
            left, right = start, end
            pivot = self.arr[(left+right)//2]
            while left <= right:
                while left <= right and self.arr[left] < pivot:
                    left += 1
                while left <= right and self.arr[right] > pivot:
                    right -= 1
                if left <= right:
                    self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
                    left, right = left+1, right-1
            if k <= right:
                _quickSelect(start=start, end=right, k=k)
            if k >= left:
                _quickSelect(start=left, end=end, k=k)

        # O(n)
        _quickSelect(start=0, end=len(self.arr)-1, k=len(self.arr)-self.top_k) # k largest = (len- k) smallest
        # O(klogk)
        sorted_topK = sorted(self.arr[-self.top_k:], reverse=True)
        return sorted_topK
```
#### Remark:
- 
#### Submission:
```
571 ms
time cost
·
6.10 MB
memory cost
·
Your submission beats
11.20 %
Submissions
```
#### Complexity:
| QuickSelect | add() | topk() | Total |
|---|---|---|---|
| Time | O(1) | O(n+klogk) |  |
| Space |  |  | O(n) |

## Heap = O(nLogk) topk; O(logn) add
```python
from heapq import heappush, heappop

class Solution:

    def __init__(self, k):
        self.k = k
        self.heap = []
        
    def add(self, num): # O(logk)
        heappush(self.heap, num)
        if len(self.heap) > self.k:
            heappop(self.heap)

    def topk(self): # O(klogk)
        return sorted(self.heap, reverse=True)
```
#### Remark:
- 同理[Lint612](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LintCode_612_K-Closest-Points.md)，雖然乍看是找最大的K個點，像maxHeap，會耗費O(nlogn)的時間。但是可以換一個角度想，要取K個最大的點，可以維護K個點的heap就好->minHeap。
#### Submission:
```
528 ms
time cost
·
6.17 MB
memory cost
·
Your submission beats
45.20 %
Submissions
```
#### Complexity:
| Heap | add() | topk() | Total |
|---|---|---|---|
| Time | O(logk) | O(klogk) |  |
| Space |  |  | O(n) |

# Summary
| Online version - Find Largest | Quick Select | MaxHeap | MinHeap |
|---|---|---|---|
| TopK | O(n+klogk) | O(klogn) | O(klogk) |
| Add | O(1) | O(logk) | O(logk) |
| Rank | A better choice when Add()>>TopK() | Worst | A better choice when TopK()>>Add() |
