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
- 模運算加減法 https://zh.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-addition-and-subtraction
    - `(A + B) % C = (A % C + B % C) % C`
    - `(A - B) % C = (A % C - B % C) % C`
- 同餘定理
    - `(A * B) % C = ((A % C) * (B % C) % C)` 
- 33進制
    ```
    abc => (a*33^2 + b*33^1 + c*33^0) % 33
        => [(a*33 + b)*33 + c] % 33
        => ((((33*0) + a % 33)*33 + b) % 33)*33 + c) % 33
    ```
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
