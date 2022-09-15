### Minimum Moves to Equal Array Elements II
https://www.lintcode.com/problem/1226/description
>Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.
```python
from typing import (
    List,
)

class Solution:
    """
    @param nums: an array
    @return: the minimum number of moves required to make all array elements equal
    """
    def min_moves2(self, nums: List[int]) -> int:
        if not nums: return -1
        median = self.QuickSelect(nums=nums, start=0, end=len(nums)-1, k=(len(nums)-1)//2)
        moves = 0
        for i in range(len(nums)):
            moves += abs(median-nums[i])
        return moves
        
    def QuickSelect(self, nums: List[int], start: int, end: int, k: int) -> int:
        # base
        if start==end:
            return nums[k]
        # recursive
        left, right = 0, len(nums)-1
        pivot = nums[(left+right)//2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left+1, right-1
        if k <= right:
            self.QuickSelect(nums=nums, start=start, end=right, k=k)
        if k >= left:
            self.QuickSelect(nums=nums, start=left, end=end, k=k)
        return nums[k]
```
#### Remark:
- Key: finding median
  - if number of elements is even, then it's okay to just pick the previous one of the middle two. 
  - Actually it's okay to just pick any number between the middle two.
- Oral Proof:
  - Case one: #elements=odd
    - just pick the middle one. Base case is n=3, where the median lies in the middle of two numbers. 
  - Case two: #elements=even
    - Base case is n=2. It's okay to randomly pick any number between [n1, n2] because the moves all sum up equally.     
#### Submission:
```
102 ms
time cost
·
6.63 MB
memory cost
·
Your submission beats
19.29 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(1)
