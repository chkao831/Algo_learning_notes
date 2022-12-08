### Implement strStr()
https://www.lintcode.com/problem/13/description?showListFe=true&page=1&problemTypeId=2&pageSize=50
>For a given `source` string and a `target` string, you should output the first index of `target` string in the `source` string. If the `target` does not exist in `source`, just return `-1`.
```python
class Solution:
    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        len_s = len(source)
        len_t = len(target)
        for i in range(len_s - len_t + 1):
            j = 0
            while (j < len_t):
                if source[i + j] != target[j]:
                    break
                j += 1
            if j == len_t:
                return i
        return -1
```
#### Remark:
- 
#### Submission:
```
1 ms
time cost
·
5.94 MB
memory cost
·
Your submission beats
98.00 %
Submissions
```
#### Complexity:
- Time: O(N)
- Space: O(1)
