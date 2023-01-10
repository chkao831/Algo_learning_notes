### Remove Duplicates from Sorted Array II
https://www.lintcode.com/problem/101/description
>Given a **sorted** array nums, logically remove the duplicates in place and return the length len, such that each element appear **at most twice** in the first len elements of the original array nums.
>If a number appears more than two times, then keep the number appears twice in array after remove.
>
>**Need to operate in the original array.**
```python
class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):

        left, right = 2, 2
        
        while right < len(nums):
            while right < len(nums) and nums[right] == nums[left - 2]:
                right += 1
            if right < len(nums):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
                
        return left
```
#### Remark:
- 快慢雙指針
#### Submission:
```
895 ms
time cost
·
8.27 MB
memory cost
·
Your submission beats
93.00 %
Submissions

```
#### Complexity:
- Time: O(n)
- Space: O(1)
