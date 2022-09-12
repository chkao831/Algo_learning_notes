### Sort Array By Parity II
https://leetcode.com/problems/sort-array-by-parity-ii/
>Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
>
>Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
>
>Return any answer array that satisfies this condition.\
> Follow Up: Could you solve it in-place?
```python
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        if not nums or len(nums)<2: return []
        left, right = 0, len(nums)-1
        # make even all left; make odd all right
        while left <= right:
            while left <= right and nums[left]%2==0:
                left+= 1
            while left <= right and nums[right]%2==1:
                right-=1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left+1, right-1
        # [evens, odds]
        l, r = 1, len(nums)-2
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+2, r-2
        return nums
```
#### Remark:
- In place partition.
- Resembles [Lint373](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_373_Partition-Array-by-Odd-and-Even.md)
#### Submission:
```
Runtime: 461 ms, faster than 15.09% of Python3 online submissions for Sort Array By Parity II.
Memory Usage: 16.3 MB, less than 74.53% of Python3 online submissions for Sort Array By Parity II.
```
#### Complexity:
- Time: O(n)
- Space: O(1)
