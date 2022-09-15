### Second Max of Array
https://www.lintcode.com/problem/479/
>Find the second max number in a given array.
```python
from typing import (
    List,
)

class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def second_max(self, nums: List[int]) -> int:
        first, second = float('-inf'), float('-inf')
        for num in nums:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num
        return second
```
#### Remark:
- Quick Select would work, too. Would also cost O(n) time and O(1) space.
#### Submission:
```
81 ms
time cost
·
5.97 MB
memory cost
·
Your submission beats
95.60 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(1)
