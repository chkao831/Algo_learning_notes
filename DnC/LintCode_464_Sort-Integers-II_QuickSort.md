### Sort Integers II
https://www.lintcode.com/problem/464/
>Given an integer array, sort it in ascending order in place. Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.
```python
from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers2(self, a: List[int]):
        self.quickSort(nums=a, start=0, end=len(a)-1)

    def quickSort(self, nums: List[int], start: int, end: int):
        # base case
        if (start >= end): return 
        # recursive case
        left, right = start, end
        pivot = nums[(left+right)//2]
        while (left <= right):
            while (left <= right and nums[left] < pivot): # nums[left] supposed to be left
                left += 1
            while (left <= right and nums[right] > pivot): # nums[right] supposed to be right
                right -= 1
            if left <= right: # found a pair to be swapped
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        self.quickSort(nums=nums, start=start, end=right)
        self.quickSort(nums=nums, start=left, end=end)
```
#### Remark:
- the `while` loop highly resembles [Partition](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_31_Partition-Array.md), except that the partition is **not strict**. This is to avoid easily downgrading to O(n^2) time complexity. If we strictly partition the `==pivot` numbers into left or right, we would easily jump to the worst case of quick sort (O(n^2) time). 
    - An example of this: `[1, 1, 1]`. The pivot is `1`. With `nums[left] <= pivot`, ending `left=3` and `right=2`, and we only fall into the if statement once and move by one step at this round. 
    - ideal pivot: 均勻劃分; worst pivot: 最大/小值
- `left <= right`, not `left < right`. 
  - Reason: Under the following scenario, if it were `<`, would directly jump out of all while loops. Then we wouldn't know if `n2` belongs to left or right partition. With `<=`, one of the inner while loop would agree and the pointer would be moved by a step. Hence, the left pointer would ***always*** point to the first index of the right partition. 
  ```
  n1| n2 |n3
      ^^
      lr 
  ``` 
#### Submission:
```
1118 ms
time cost
·
17.68 MB
memory cost
·
Your submission beats
78.00 %
Submissions
```
#### Complexity:
- Time: O(nlogn) (n: partition; logn: depth)
- Space: O(logn)
