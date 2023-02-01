### Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
>Given two strings `str1` and `str`2, return the largest string `x` such that `x` divides both `str1` and `str2`.

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        # let str1 be the larger one, swap if needed
        if len1 < len2:
            str1, str2 = str2, str1

        if str1 == str2:
            return str1
        
        if str1[:len(str2)] == str2: # keep dividing
            return self.gcdOfStrings(str1[len(str2):], str2)
        else: # if the first part of str1 is not equal to str2, then failed
            return ""
```
#### Remark:
- https://www.youtube.com/watch?v=06oWnxVIAv0
#### Submission:
```
Runtime
35 ms
Beats
70.52%

Memory
13.8 MB
Beats
70.81%
```
#### Complexity:
- Time: O(len(str1) + len(str2))
- Space: O(len(str1) + len(str2))
