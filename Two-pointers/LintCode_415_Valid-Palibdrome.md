https://www.lintcode.com/problem/415/description

```python
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def is_palindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not self.is_valid(s[left]):
                left += 1
            while left < right and not self.is_valid(s[right]):
                right -= 1
            if left < right and s[right].lower() != s[left].lower():
                return False
            left += 1
            right -= 1
        return True

    def is_valid(self, char: str) -> bool:
        return char.isalpha() or char.isdigit()

```

#### Remark
- used **<=** instead of **<**
- forgot **.lower()** conversion
- isalpha() **or** isdigit(), not **and**
