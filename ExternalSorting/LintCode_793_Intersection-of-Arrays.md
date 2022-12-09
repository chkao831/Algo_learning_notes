# Intersection of Arrays
https://www.lintcode.com/problem/793/
>

## 1. Hashmap (defaultdict as a counter)
### 1.1 Addition
```python
from typing import (
    List,
)
from collections import defaultdict

class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersection_of_arrays(self, arrs: List[List[int]]) -> int:
        counter = defaultdict(int)
        for arr in arrs:
            for num in arr:
                counter[num] += 1

        # because there are no duplicated elements in each array
        output_counts = 0
        for val, count in counter.items():
            if count == len(arrs):
                output_counts += 1
        return output_counts
```
#### Remark:
- 關鍵：集中的元素一定在每一個數組中都出現過，所以交集中的元素在所有數組中的出現次數一定等於數組個數。

#### Submission:
```
102 ms
time cost
·
11.20 MB
memory cost
·
Your submission beats
87.40 %
Submissions
```
### 1.2 Subtraction
```python
from typing import (
    List,
)
from collections import defaultdict
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersection_of_arrays(self, arrs: List[List[int]]) -> int:
        counter_subtraction = defaultdict(int)
        ideal_count = len(arrs)
        for num in arrs[0]:
            counter_subtraction[num] = ideal_count
        output_counts = 0
        for arr in arrs:
            for num in arr:
                counter_subtraction[num] -= 1
                if counter_subtraction[num] == 0:
                    output_counts += 1
        return output_counts
```
#### Remark:
- 關鍵：集中的元素一定在每一個數組中都出現過，所以交集中的元素在所有數組中的出現次數一定等於數組個數。
- 和加法概念基本相同，只是用減的，減到零就是都有出現的。

#### Submission:
```
102 ms
time cost
·
11.20 MB
memory cost
·
Your submission beats
87.40 %
Submissions
```
### Complexity:
- Time: O(N)
- Space: O(N)


## 2. Heap
```python
from typing import (
    List,
)
from heapq import heappush, heappop
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersection_of_arrays(self, arrs: List[List[int]]) -> int:
        heap = []
        for arr_idx, sub_head in enumerate(arrs):
            if not sub_head:
                return 0
            else:
                sub_head.sort()
                heappush(heap, (sub_head[0], arr_idx, 0))

        recorder_count, recorder_val = 0, 0
        intersected = 0
        while heap:

            ele, arr_idx, ele_idx = heappop(heap)
            if ele > recorder_val:
                recorder_count, recorder_val = 1, ele
            else: # ele == recorder_val
                recorder_count = recorder_count+1
                if recorder_count == len(arrs):
                    intersected += 1

            if ele_idx+1 < len(arrs[arr_idx]):
                heappush(heap, (arrs[arr_idx][ele_idx+1], arr_idx, ele_idx+1))

        return intersected
```
#### Remark:
- heap的元素由(值的內容, 是在第幾個array, 是在該array排第幾個位子）組成，同理[Lint577-Merge K Sorted Interval Lists](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_577_Merge-K-Sorted-Interval-Lists.md)
- 因為minHeap元素值從小pop出來，所以**用if-else比較當前的值，只可能是大於或等於**。
#### Submission:
```
284 ms
time cost
·
11.32 MB
memory cost
·
Your submission beats
8.60 %
Submissions
```
#### Complexity:
Assume there're k sublists; each sublist has n elements. \
There're k*n = N elements in total.
- Time: O(knlogn + klogk + nlogk)
    - 前半段sublist in-place sort + push頭進去堆 = O(knlogn+klogk)
    - 後半段while heap = O(nlogk)
- Space: O(k) (堆維持著k個元素）
