### Move Zeroes
https://www.lintcode.com/problem/539/
>Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

<img src="../images/539_Move-Zeroes.png" width="700px" />

```python
from typing import (
    List,
)

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def move_zeroes(self, nums: List[int]):
        if not nums or len(nums)<2: return
        fill_ptr, move_ptr = 0, 0
        while move_ptr < len(nums):
            if nums[move_ptr] != 0:
                if nums[fill_ptr] != nums[move_ptr]:
                    # replacement, not swap
                    nums[fill_ptr] = nums[move_ptr]
                fill_ptr += 1
            move_ptr += 1 # always
        # make remaining digits zero
        while fill_ptr < len(nums):
            if(nums[fill_ptr]!=0):
                nums[fill_ptr] = 0
            fill_ptr += 1

```

#### Remark:
- Method is tricky. Need to review. 
#### Submission:
```
101ms
Time Cost

7.26MB
Memory Cost

93.20%
Beats
```
#### Complexity:
- Time: O(n)
- Space: O(1)
