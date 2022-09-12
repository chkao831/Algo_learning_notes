### Partition Array by Odd and Even
> Partition an integers array into odd number first and even number second.
>
> Example\
> Given [1, 2, 3, 4], return [1, 3, 2, 4]
> 
> Challenge\
> Do it in-place.
```python
class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        if not nums or len(nums)<2:
            return []
        left, right = 0, len(nums)-1
        while left <= right:
            while left <= right and nums[left]%2 == 1:
                left += 1
            while left <= right and nums[right]%2 == 0:
                right -= 1
            if left <= right:
                nums[left], num[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums
```
#### Remark:
- 

#### Complexity:
- Time: O(n)
- Space: O(1)
