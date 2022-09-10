https://www.lintcode.com/problem/57/

```python
from typing import (
    List,
)

class Solution:
    def __init__(self):
        self.results = []

    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        """
        @param numbers: an array numbers of n integer; might contain duplications. 
        @return: Find all unique triplets in the array which gives the sum of zero.
                Can be in any order, but must not contain duplicated triplets.
        """
        if not numbers or len(numbers)<3:
            return self.results

        numbers.sort() #nlog(n)

        # for 3 points, I assign the basis to be the smallest value
        for i in range(0, len(numbers)-2): # O(n) loops * O(n) of two_sum_calc_call = O(n^2)
            # skip for basis duplication
            if i > 0 and numbers[i] == numbers[i-1]: continue
            # otherwise, start assigning pointers
            left = i + 1
            right = len(numbers)-1
            target = -numbers[i]
            self.two_sum_calc(numbers, left, right, target)
        return self.results

    def two_sum_calc(self, numbers, left, right, target):
        while left < right:
            if (numbers[left] + numbers[right] == target):
                self.results.append([-target, numbers[left], numbers[right]])
                left += 1
                right -= 1
                # skip for left & right pointer duplication
                while left < right and numbers[left] == numbers[left-1]: 
                    left += 1
                while left < right and numbers[right] == numbers[right+1]: 
                    right -= 1
            elif (numbers[left] + numbers[right] < target):
                left += 1
            else: 
                right -= 1
```
#### Remark:
- need to remember edge case
- for calculation efficiency, should skip basis pointer calculation through continue before two sum calculation
- for calculation efficiency, should check for each pointer if the value is duplicated from the previous step; if so, shift. 
- A mistake: `target = -self.numbers[i]`, not `target = self.numbers[i]`
#### Submission:
```
86 ms
time cost
·
5.99 MB
memory cost
·
Your submission beats
42.40 %
Submissions
```
#### Complexity:
- Time: O(nlogn) + O(n^2)
- Space: O(k), where k=number of solution(s)
