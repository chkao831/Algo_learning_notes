### Ugly Number
https://leetcode.com/problems/ugly-number/
>An ugly number is a positive integer whose prime factors are limited to `2`, `3`, and `5`.
>
>Given an integer `n`, return true if `n` is an ugly number.
```python
class Solution:
    def isUgly(self, n: int) -> bool:
        
        def _divideByDivisor(num: int, divisor: int) -> int:
            while num % divisor == 0:
                num = num // divisor
            return num
        
        if n < 1:
            return False
        for divisor in [2,3,5]:
            n = _divideByDivisor(n, divisor)
        return n == 1
```
#### Remark:
- Link to [Ugly Number II](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LeetCode_264_Ugly-Number-II.md)
#### Submission:
```
Runtime: 78 ms, faster than 5.99% of Python3 online submissions for Ugly Number.
Memory Usage: 13.8 MB, less than 58.69% of Python3 online submissions for Ugly Number.
```
#### Complexity:
- Time: When dividing an integer `x` by `y`, there can be at most O(log_y(x))divisions.
  - 3(log(x)) => O(logN) 
- Space: O(1)
