### First Unique Number in Data Stream
https://www.lintcode.com/problem/685/description
>Given a continuous stream of data, write a function that returns the first unique number (including the last number) when the terminating number arrives. \
>If the terminating number is not found, return `-1`.

Online Algorithm (在線算法) version: [Leet1429 - First Unique Number](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_1429_First-Unique-Number.md) 只遍歷一次，使用Singly Linked Node + Hashmap。

```python
from typing import (
    List,
)
from collections import deque

class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def first_unique_number(self, nums: List[int], number: int) -> int:
        queue = deque([])
        for num in nums:
            queue.append(num)
            if num == number:
                break
        else: # is executed only when the loop is NOT terminated by a break statement
            return -1 # terminating number not found
        for num in queue:
            if queue.count(num) == 1:
                return num
        return -1
```
#### Remark:
- The `else` block just after `for/while` is executed **only when the loop is NOT terminated by a break statement**.
#### Submission:
```
102 ms
time cost
·
11.28 MB
memory cost
·
Your submission beats
87.20 %
Submissions
```
#### Complexity:
- Time: Counting how many times a given item appears in the queue has a cost of O(N). This is true even for the library functions we're using. At a cost of O(N) each time, this gives us a cost of O(N^2).
- Space: O(N)
