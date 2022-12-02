## Convert a Number to Hexadecimal
https://www.lintcode.com/problem/1253/description
>給定一個整數，寫一個函數將其轉換為16進制。

### Concept
- Decimal -> Hexadecimal
  - base 10 -> base 16
  - Example
    - (D) 479 / 16 = 29 R 15 ~ F (H, LSD)\
      => 29 / 16 = 1 R 13 ~ D (H)\
      => 1 / 16 = 0 R 1 ~ 1 (H, MSD)\
      => 1DF (H)
    - (D) 33 / 16 = 2 R 1\
      => 2 / 16 = 0 R 2\
      => 21 (H)
- The given number is guaranteed to fit within the range of a 32-bit signed integer.      
  - 至多32位Binary -> 至多8位Hexadicimal
- 與運算
  - 15 (D) -> 1111 (B)
  - Example
    - 33 (100001) & 15(1111) = (0001) = 1 \
      => (10) & (1111) = (10) = 2\
      => 21 (H)

```python
HEX = "0123456789abcdef"

class Solution:
    """
    @param num: an integer
    @return: convert the integer to hexadecimal
    """
    def to_hex(self, num: int) -> str:
        if num == 0:
            return 0
        str_out, digit_count = "", 0
        while digit_count < 8 and num != 0:
            four_bit = HEX[num & 15]
            str_out = four_bit + str_out
            num = num >> 4
            digit_count += 1
        return str_out
```
#### Remark:
- （1）由數字範圍為32位有符號整數範圍可知，十六進制的最大位數為8
- （2）通過與運算，獲得低位的十六進制值
- （3）通過右移運算，將高位的十六進制值移到低位，從而獲取該值


#### Submission:
```
101 ms
time cost
·
6.03 MB
memory cost
·
Your submission beats
65.62 %
Submissions
```
#### Complexity:
- Time: O(L)
- Space: O(L)
