### Add and Search
https://www.lintcode.com/problem/716/description/
> Given two integer arrays `inputs` and `tests`, write a function that will return TRUE if there exists any pair in `inputs`, whose sum could be found in `tests`. Otherwise, return FALSE.
#### Hashmap Approach: O(n^2) time, O(n) space
```python
from typing import (
    List,
)

class Solution:
    """
    @param inputs: an integer array
    @param tests: an integer array
    @return: return true if sum of two values in inputs are in tests.
    """
    def add_and_search(self, inputs: List[int], tests: List[int]) -> bool:
        for t in tests:
            hash_t = set() # any of two does not include oneself with oneself
            for i in inputs:
                complement = t - i
                if complement in hash_t: 
                    return True
                hash_t.add(i)
        return False
```
#### TwoPointer Approach: O(nlogn)+O(n^2) time, O(1) space
```python
from typing import (
    List,
)

class Solution:
    """
    @param inputs: an integer array
    @param tests: an integer array
    @return: return true if sum of two values in inputs are in tests.
    """
    def add_and_search(self, inputs: List[int], tests: List[int]) -> bool:
        inputs.sort() #nlogn
        for t in tests: #n*n
            left, right = 0, len(inputs)-1
            while left < right:
                if inputs[left] + inputs[right] == t: return True
                elif inputs[left] + inputs[right] < t:
                    left += 1
                else: # >t
                    right -= 1
        return False
```
#### Remark:
- Remember it's `while left < right` without equal sign in TwoPointer Approach, because oneself cannot sum up with itself.
#### Submission:
```
81 ms
time cost
·
6.03 MB
memory cost
·
Your submission beats
80.00 %
Submissions
```
```
81 ms
time cost
·
5.98 MB
memory cost
·
Your submission beats
80.00 %
Submissions
```
