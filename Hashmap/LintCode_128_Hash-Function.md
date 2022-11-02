### Hash Function
https://www.lintcode.com/problem/128/description
>
```python
MAGIC = 33

class Solution:
    
    def hash_code(self, key: str, hashsize: int) -> int:
        """
        @param key: A string you should hash
        @param hashsize: An integer
        @return: An integer
        """

        out = 0
        for char in key:
            out = (out * MAGIC + ord(char)) % hashsize
        return out
```
#### Remark:
- 
#### Submission:
```
102 ms
time cost
·
6.18 MB
memory cost
·
Your submission beats
48.80 %
Submissions
```
#### Complexity:
- Time:
- Space:
