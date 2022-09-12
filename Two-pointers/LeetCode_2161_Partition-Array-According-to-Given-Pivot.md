### Partition Array According to Given Pivot
https://leetcode.com/problems/partition-array-according-to-given-pivot/
>You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:
>
>Every element less than pivot appears before every element greater than pivot.\
> Every element equal to pivot appears in between the elements less than and greater than pivot.\
> The **relative order** of the elements less than pivot and the elements greater than pivot is **maintained**.
```python
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr = [pivot]*len(nums)
        left, right = 0, len(nums)-1
        for i in range(len(nums)):
            if nums[i] < pivot: # traverses from left to right
                arr[left], left = nums[i], left+1
            if nums[~i] > pivot: # ~i means -i - 1; traverses from right to left
                arr[right], right = nums[~i], right-1
        return arr
```
Also, a 1-line solution:
```python
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return [i for i in nums if i < pivot] + [j for j in nums if j == pivot] + [k for k in nums if k > pivot]
```
#### Remark:
- The relative order less/greater than pivot is maintained. 
#### Submission:
```
Runtime: 3463 ms, faster than 6.80% of Python3 online submissions for Partition Array According to Given Pivot.
Memory Usage: 31.7 MB, less than 36.96% of Python3 online submissions for Partition Array According to Given Pivot.
```
```
Runtime: 4948 ms, faster than 5.00% of Python3 online submissions for Partition Array According to Given Pivot.
Memory Usage: 31.7 MB, less than 36.96% of Python3 online submissions for Partition Array According to Given Pivot.
```
#### Complexity:
- Time: O(n)
- Space: O(n)
