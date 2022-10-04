### Find Letter
https://www.lintcode.com/problem/1820/description
>給定一個字符串str，返回字符串中字母順序最大的而且同時在字符串中出現大寫和小寫的字母。
>如果不存在這樣的字母，返回‘~‘
```python
class Solution:
    """
    @param str: the str
    @return: the letter
    """
    def find_letter(self, str: str) -> str:
        char_2dList = [[0 for j in range(2)] for i in range(26)] # 26*2 array
        for char in str:
            if ord('a') <= ord(char) <= ord('z'):
                char_2dList[ord(char)-ord('a')][0] = 1
            else:
                char_2dList[ord(char)-ord('A')][1] = 1
        for idx in range(25, -1, -1):
            if char_2dList[idx][0] == 1 and char_2dList[idx][1] == 1:
                return chr(idx + ord('A'))
        return '~'
```
#### Remark:
- ord()

Format: ord(c), c: character

傳入字元，回傳對應的Unicode字元。

>>> ord('a')
97
#### Submission:
```
101 ms
time cost
·
5.96 MB
memory cost
·
Your submission beats
53.18 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(1) (O(26))
