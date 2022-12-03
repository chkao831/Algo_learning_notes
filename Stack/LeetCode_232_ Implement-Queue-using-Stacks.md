###  Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/
>Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
>
>Implement the `MyQueue` class:
>
>`void push(int x)` Pushes element `x` to the back of the queue.\
>`int pop()` Removes the element from the front of the queue and returns it.\
>`int peek()` Returns the element at the front of the queue.\
>`boolean empty()` Returns `true` if the queue is empty, `false` otherwise.

<p>
    <img src="https://leetcode.com/media/original_images/232_queue_using_stacksAPop.png" width="700" />
</p>
                                                
```python
class MyQueue:

    def __init__(self):
        self.dumping_stack = []
        self.dumped_stack = []

    def push(self, x: int) -> None:
        self.dumping_stack.append(x)

    def _ask_from_dumping_stack(self):
        if not self.dumped_stack: # dump only when the dumped stack is empty
            while self.dumping_stack:
                self.dumped_stack.append(self.dumping_stack.pop())
        
    def pop(self) -> int:
        self._ask_from_dumping_stack()
        return self.dumped_stack.pop()
        
    def peek(self) -> int:
        self._ask_from_dumping_stack()
        return self.dumped_stack[-1]

    def empty(self) -> bool:
        self._ask_from_dumping_stack()
        return not self.dumped_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```
#### Remark:
- 方法：push東西到`dumping_stack`，當需要pop出來的時候，看一下`dumped_stack`，如果是有東西的就拿，如果沒東西就從`dumping_stack`倒。
#### Submission:
```
Runtime: 56 ms, faster than 46.67% of Python3 online submissions for Implement Queue using Stacks.
Memory Usage: 14 MB, less than 24.23% of Python3 online submissions for Implement Queue using Stacks.
```
#### Complexity:
- Time:
  - `push()` O(1)
  - `pop()` O(1) on average, O(n) max
  - `peek()` O(1) on average, O(n) max
  - `empty()` O(1) on average, O(n) max
- Space: O(n)
