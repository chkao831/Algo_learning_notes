### Plus One
https://www.lintcode.com/problem/407/description
>Description\
> Given a non-negative number represented as an array of digits, plus one to the number.\
> Returns a new array.
>
>The number is arranged according to the number of digits, with the highest digit at the top of the list.
```python
from typing import (
    List,
)

class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plus_one(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i+1, len(digits)):
                    digits[j] = 0
                return digits
        return [1] + [0] * len(digits)
```
#### Remark:
- To return a zero array, use `[0]*length`
- Made a mistake: `if digits[i] != 9`, not `if i != 9`
#### Submission:
```
81 ms
time cost
·
6.01 MB
memory cost
·
Your submission beats
97.40 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(1)
