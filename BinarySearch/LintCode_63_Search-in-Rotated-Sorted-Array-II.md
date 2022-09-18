### Search in Rotated Sorted Array II
https://www.lintcode.com/problem/search-in-rotated-sorted-array-ii/description

>Suppose a sorted array is rotated at some pivot unknown to you beforehand.
>
>(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
>
>You are given a target value to search. If found in the array return its index, otherwise return -1.\
>**What if duplicates are allowed?**
>**Would this affect the run-time complexity? How and why?**
>
>Write a function to determine if a given target is in the array.
```python
from typing import (
    List,
)

class Solution:
    """
    @param a: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean 
    """
    def search(self, a: List[int], target: int) -> int:
        # write your code here
        def trough_binary_search() -> int:
            start, end = 0, len(a)-1
            while start + 1 < end:
                mid = (start+end)//2
                if a[mid] < a[end]:
                    end = mid
                elif a[mid] == a[end]:
                    end -= 1
                else: # a[mid] > a[end]
                    start = mid
            return start if a[start]<=a[end] else end

        def pivot_binary_search(trough: int) -> bool:
            if (a[trough] <= target <= a[-1]):
                left, right = trough, len(a)-1
            else:
                left, right = 0, trough-1
            while left + 1 < right:
                mid = (left+right)//2
                if a[mid] < target:
                    left = mid
                elif a[mid] == target:
                    right -= 1
                else: # a[mid] > target
                    right = mid
            if a[left] == target:
                return True
            if a[right] == target:
                return True
            return False

        if not a: 
            return False
        trough = trough_binary_search()
        return pivot_binary_search(trough)
```
#### Remark:
- This is slightly adjusted from [Lint62](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_62_Search-in-Rotated-Sorted-Array.md) 方法一, except that
  - use [Lint160](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_160_Find-Minimum-in-Rotated-Sorted-Array-II.md) remark, when `a[mid] == a[end]`, `end-=1` and then when `a[mid] == target`, return `True`
#### Submission:
```
101 ms
time cost
·
7.50 MB
memory cost
·
Your submission beats
46.60 %
Submissions
```
#### Complexity:
- Time: O(logn) on average, while falls to O(n) in worst case
- Space: O(1)
