### Next Permutation
https://leetcode.com/problems/next-permutation/
>Given an array of integers `nums`, find the next permutation of `nums`.

<p>
    <img src="https://leetcode.com/media/original_images/31_Next_Permutation.gif" width="500" />
</p>

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(idx1: int, idx2: int):
            nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
            return
    
        def reverse(startingIndex: int):
            left, right = startingIndex, len(nums)-1
            while left < right:
                swap(left, right)
                left, right = left+1, right-1
            return
        
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # i is at the first decreasing index
        if i >= 0:
            j = len(nums) - 1
            while nums[i] >= nums[j]:
                j -= 1
            swap(i, j)
        reverse(i+1)
```
#### Remark:
- Use two pointer (in `reverse`) to reverse the whole array.
#### Submission:
```
Runtime: 90 ms, faster than 22.83% of Python3 online submissions for Next Permutation.
Memory Usage: 13.7 MB, less than 98.28% of Python3 online submissions for Next Permutation.
```
#### Complexity:
- Time: O(n)
- Space: O(1)
