### Evaluate Reverse Polish Notation 
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
>Evaluate the value of an arithmetic expression in Reverse Polish Notation.
>
>Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.
>
>**Note that division between two integers should truncate toward zero.**
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop()+stack.pop())
            elif token == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == "*":
                stack.append(stack.pop()*stack.pop())
            elif token == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int (a / b))
            else:
                stack.append(int(token))
        return stack.pop()
```
#### Remark:
- Note that division between two integers should truncate toward zero: https://stackoverflow.com/questions/19919387/in-python-what-is-a-good-way-to-round-towards-zero-in-integer-division
  - ```python
    >>> -1/2
    -0.5
    >>> -1 // 2
    -1
    >>> int(-1/2)
    0
    >>> int(1/2)
    0
    ```
#### Submission:
```
Runtime
65 ms
Beats
96.64%

Memory
14.3 MB
Beats
60.78%
```
#### Complexity:
- Time: O(n)
- Space: O(n)
