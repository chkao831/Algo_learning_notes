## Search in Rotated Sorted Array
https://www.lintcode.com/problem/62/
>Suppose a sorted array is rotated at some pivot unknown to you beforehand.
>
>(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
>
>You are given a target value to search. If found in the array return its index, otherwise return -1.
>
>**You may assume no duplicate exists in the array.**

### 方法一：
#### 思路:
先用[Lint159](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_159_Find-Minimum-in-Rotated-Sorted-Array.md)方法做一次二分，找到低谷，然後擇一方繼續二次二分
#### 代碼:
```python
from typing import (
    List,
)

class Solution:
    """
    @param a: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, a: List[int], target: int) -> int:
        
        def trough_binary_search() -> int:
            start, end = 0, len(a)-1
            while start + 1 < end:
                mid = (start+end)//2
                if a[mid] <= a[end]:
                    end = mid
                else:
                    start = mid
            return start if a[start]<=a[end] else end

        def pivot_binary_search(trough: int) -> int:
            if (a[trough] <= target <= a[-1]):
                left, right = trough, len(a)-1
            else:
                left, right = 0, trough-1
            while left + 1 < right:
                mid = (left+right)//2
                if a[mid] >= target:
                    right = mid
                else:
                    left = mid
            if a[left] == target:
                return left
            if a[right] == target:
                return right
            return -1

        if not a: 
            return -1
        trough = trough_binary_search()
        return pivot_binary_search(trough)
```
#### Submission:
```
81 ms
time cost
·
6.76 MB
memory cost
·
Your submission beats
99.80 %
Submissions
```

### 方法二：
#### 思路
```
             target
                v
OOO............OXX.......X
  ↗
 ↗
               ↗ 
             ↗
           ↗

如果target落在右下，X的條件為：t<=X1<last
如果target落在左上，X的條件為：X1>=t or X1<first
思路太複雜

於是 可以：
在一個rotated sorted array上切一刀，可以判斷出這一刀切在
rotation的左上半部分 還是右下半部分
劈出mid, mid>=start, 則在左上, otherwise(<start)則在右下，這兩個部分是沒有交集的
然後判斷target若是介於middle~end之間 往右邊去 反之往左邊去
這一刀的兩邊仍然是rotated sorted array
這樣的條件可以允許我們下一步繼續二分
```
#### 代碼:
```python
from typing import (
    List,
)

class Solution:
    """
    @param a: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, a: List[int], target: int) -> int:
        
        def integrated_binary_search() -> int:
            start, end = 0, len(a)-1
            while start+1 < end:
                mid = (start+end)//2
                if a[mid] >= a[start]: # upper left
                    if a[start] <= target <= a[mid]: # further left
                        end = mid
                    else:
                        start = mid
                else: # a[mid] < a[start], falls in lower right portion
                    if a[mid] <= target <= a[end]:
                        start = mid
                    else:
                        end = mid
            if a[start] == target: return start
            if a[end] == target: return end
            return -1

        if not a: 
            return -1
        return integrated_binary_search()
```
#### Submission:
```
124 ms
time cost
·
8.23 MB
memory cost
·
Your submission beats
12.00 %
Submissions
```
#### Complexity:
- Time: Both yield O(logn), although method 1 uses binary search twice
- Space: O(1)
