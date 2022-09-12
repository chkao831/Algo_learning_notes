### Interleaving Positive and Negative Numbers
https://www.lintcode.com/problem/144/description
>Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.
```python
from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array.
    @return: nothing
    """
    def rerange(self, a: List[int]):
        neg_count = self.partition(a) # right start
        pos_count = len(a) - neg_count
        # if neg > pos, then left pointer forward by 1 step: n n n p p
        #                                                      ^     ^ and vice versa
        # if neg == pos, then both pointers forward by 1
        left = 1 if neg_count >= pos_count else 0
        right = len(a)-2 if pos_count >= neg_count else len(a)-1

        return self.interleave(a, left, right)
    
    def partition(self, a: List[int]):
        threshold = 0
        left, right = 0, len(a)-1
        while left <= right:
            while (left <= right and a[left] < threshold):
                left += 1
            while (left <= right and a[right] >= threshold):
                right -= 1
            if (left <= right):
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1
        return left # first index of right partition

    def interleave(self, a: List[int], left: int, right: int):
        while left < right:
            a[left], a[right] = a[right], a[left]
            left, right = left+2, right-2
        return a
```
#### Remark:
- If the given array is already sorted (which is not guaranteed in this case), then the partition step could be skipped.
- Key: No need to spend O(nlogn) to sort. The key is to **(1) Partition then (2) Interleave**. 
- Depending on which of the number of negative/positive numbers dominates, the starting position of the interleaving pointers may differ by one step.

#### Complexity:
- Time: O(n)
- Space: O(1) in place

#### Notes:
- In Python, when passing **mutable objects**, it could be considered as **call by reference** because as their values change inside the function, they will also be reflected outside the function.
  - As an example, in the code above, since `a: List[int]` is mutable, after we call `self.partition(a)`, the array `a` is modified in place. 
- Contrarily, when passing immutable objects (like strings), once we leave the scope of function, the modification is no longer in the name space, and the value that the string refers to was never changed.
