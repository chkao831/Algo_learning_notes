### Calculate number
https://www.lintcode.com/problem/1665/description
>Given a decimal number num, now you need to convert it to a binary number and return the sum of 1 and the every position of 1.

```python
from typing import (
    List,
)
from functools import reduce

class Solution:
    """
    @param num: the num
    @return: the array subject to the description
    """
    def calculate_number(self, num: int) -> List[int]:
        binary_num  = format(num, 'b')
        list_binary_num = [*binary_num] # to list of string
        list_binary_num = [eval(i) for i in list_binary_num] # to list of int
        reduced = [reduce(lambda x,y: x+y, list_binary_num)]
        for idx, val in enumerate(list_binary_num):
            if val == 1:
                reduced.append(idx+1)
        return reduced
```
#### Remark:
- 
#### Submission:
```
81 ms
time cost
·
6.02 MB
memory cost
·
Your submission beats
90.48 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(n)
