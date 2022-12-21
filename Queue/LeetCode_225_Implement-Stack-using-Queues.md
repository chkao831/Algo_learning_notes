### Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/
>Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
>
>Implement the `MyStack` class:
>
>`void push(int x)` Pushes element `x` to the top of the stack.\
>`int pop()` Removes the element on the top of the stack and returns it.\
>`int top()` Returns the element on the top of the stack.\
>`boolean empty()` Returns `true` if the stack is empty, `false` otherwise.

<p>
    <img src="https://leetcode.com/media/original_images/225_stack_using_queues_popA.png" width="600" />
</p>

```python
from collections import deque

class MyStack:

    def __init__(self):
        self.main_deque = deque()
        self.buffer_deque = deque()

    def push(self, x: int) -> None:
        self.main_deque.append(x)

    def pop(self) -> int:
        n = len(self.main_deque)
        for _ in range(n-1):
            self.buffer_deque.append(self.main_deque.popleft())
        popped = self.main_deque.popleft()
        # for _ in range(len(self.buffer_deque)):
        #     self.main_deque.append(self.buffer_deque.popleft())
        self.main_deque, self.buffer_deque = self.buffer_deque, self.main_deque
        return popped

    def top(self) -> int:
        popped = self.pop()
        self.main_deque.append(popped)
        return popped

    def empty(self) -> bool:
        return not self.main_deque


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```
#### Remark:
- 原理：`buffer_deque`常年保持淨空狀態，需要東西的時候把所有東西從`main_deque`到乾淨，除了最裡面那一個不要倒。取完以後，從`buffer_deque`再倒回來。
  - 注意：從`buffer_deque`倒回來，雖然可以用for loop，但直接swap即可。 
#### Submission:
```
Runtime: 63 ms, faster than 19.46% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 14 MB, less than 74.85% of Python3 online submissions for Implement Stack using Queues.
```
#### Complexity:
- Time:
  - `push()` O(1)
  - `pop()` **O(n)**
  - `top()` **O(n)**
  - `empty()` O(1)
- Space: O(n)
