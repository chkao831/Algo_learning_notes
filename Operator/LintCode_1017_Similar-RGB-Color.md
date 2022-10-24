### Similar RGB Color
https://www.lintcode.com/problem/1017/description
>Given the color `"#ABCDEF"`, return a 7 character color that is most similar to `#ABCDEF`, and has a shorthand (that is, it can be represented as some `"#XYZ"`)
```python
class Solution:
    def similar_r_g_b(self, color: str) -> str:

        def f(comp):
            quotient, remainder = divmod(int(comp, 16), 17) # int(value, base [optional])
            if remainder > 8: 
                quotient += 1
            return '{:02x}'.format(17 * quotient)

        return '#' + f(color[1:3]) + f(color[3:5]) + f(color[5:])
```
#### Remark:
- `int(value, base [optional])`

  ```
  >>> int('ff', 16)
  255
  >>> int('00', 16)
  0
  ```
- String Formatting in Python\
  b、d、o、x 分别是二进制、十进制、八进制、十六进制。
  ```
  >>> '{:.2f}'.format(3.1415926)
  3.14
  >>>'{:b}'.format(11)
  1011
  >>>'{:d}'.format(11)
  11
  >>>'{:o}'.format(11)
  13
  >>>'{:x}'.format(11)
  b
  >>>'{:#x}'.format(11)
  0xb
  >>>'{:#X}'.format(11)
  0XB
  ```
#### Submission:
```
325 ms
时间消耗
·
12.44 MB
空间消耗
·
您的提交打败了
82.80 %
的提交
```
#### Complexity:
- Time: O(1)
- Space: O(1)
