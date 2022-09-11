### Partition Array
https://www.lintcode.com/problem/31/description
>Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:
>
>All elements < k are moved to the left\
>All elements >= k are moved to the right\
>Return the partitioning index, i.e the first index i nums[i] >= k.
```python
from typing import (
    List,
)

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partition_array(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            while (left <= right and nums[left] < k):
                left += 1
            while (left <= right and nums[right] >= k):
                right -= 1
            if left <= right: # found a pair to be swapped
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left
```
#### Remark:
- the `while` loop highly resembles [Quick Sort](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_464_Sort-Integers-II_QuickSort.md), except that the array is strictly divided into < k part and >= k parts.
- `left <= right`, not `left < right`. 
  - Reason: Under the following scenario, if it were `<`, would directly jump out of all while loops. Then we wouldn't know if `n2` belongs to left or right partition. With `<=`, one of the inner while loop would agree and the pointer would be moved by a step. Hence, the left pointer would ***always*** point to the first index of the right partition. 
  ```
  n1| n2 |n3
      ^^
      lr 
  ``` 
#### Submission:
```
81 ms
time cost
·
6.06 MB
memory cost
·
Your submission beats
98.40 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(1)
