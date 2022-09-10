> ### 609. Two Sum - Less than or equal to target
> Given an array of integers, find how many pairs in the array such that their sum is less than or equal toa specific target number. Please return the number of pairs.
>
> Example:
>
> Given nums =[2, 7, 11, 15], target = 24.
> Return 5.\
> 2 + 7 < 24\
> 2 + 11 < 24\
> 2 + 15 < 24\
> 7 + 11 < 24\
> 7 + 15 < 24

```python
class Solution:

    def twoSum5(self, nums, target):
        """
        @param nums [int]
        @param target int
        @return an integer
        """
        left, right = 0, len(nums)-1
        count = 0
        nums.sort() # O(nlogn)
    
        while left < right:
            val = nums[left] + nums[right]
            if val > target:
                right -= 1
            else:
                count += (right - left)
                left += 1
        return count
```
#### Remark:
- `count += (right - left)`, not `count += 1`, because before moving the left pointer, we need to consider all intermediate combination with the left-pointed value. 

#### Complexity:
- Time: O(nlogn)
- Space: O(1)
