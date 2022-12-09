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
import heapq
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        p_queue = []
        for i, arr in enumerate(arrs):
            if len(arr) == 0:
                return 0
            arr.sort()
            heapq.heappush(p_queue, (arr[0], (i, 0)))
            
        last_value, count, intersection = 0, 0, 0
        while p_queue:
            val, ind_tuple = heapq.heappop(p_queue)
            if count == 0 or val != last_value:
                if count == len(arrs):
                    intersection += 1
                last_value = val
                count = 1
            else:
                count += 1
                
            new_ind_tuple = (ind_tuple[0], ind_tuple[1] + 1)
            if new_ind_tuple[1] < len(arrs[new_ind_tuple[0]]):
                val = arrs[new_ind_tuple[0]][new_ind_tuple[1]]
                heapq.heappush(p_queue, (val, new_ind_tuple))
                
        if count == len(arrs):
            intersection += 1
        return intersection
```
#### Remark:
- 
#### Submission:
```
```
#### Complexity:
- Time: O(nklogk + knlogn)
- Space: O(nk)
