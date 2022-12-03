### Max Stack
https://leetcode.com/problems/max-stack/
>Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.
>
>Implement the `MaxStack` class:
>
>`MaxStack()` Initializes the stack object.\
>`void push(int x)` Pushes element `x` onto the stack.\
>`int pop()`Removes the element on top of the stack and returns it.\
>`int top()` Gets the element on the top of the stack without removing it.\
>`int peekMax()` Retrieves the maximum element in the stack without removing it.\
>`int popMax()` Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.\
>**You must come up with a solution that supports O(1) for each top call and O(logn) for each other call.**

Approach: Heap (maxheap) + Stack + Hashset, Lazy Update

```python
from heapq import heappush, heappop

class MaxStack:

    def __init__(self):
        # stack [(item, id)]
        self.stack = []
        # max heap [(-item, -id)]
        self.heap = []
        # id counter
        self.id_ctr = 0
        # set that stores removed items
        self.mutually_removed_id = set()

    def push(self, x: int) -> None:
        self.stack.append((x, self.id_ctr))
        heappush(self.heap, (-x, -self.id_ctr))
        self.id_ctr += 1

    def _to_next_unremoved_stackTop(self):
        while self.stack and self.stack[-1][1] in self.mutually_removed_id:
            self.stack.pop()
        
    def pop(self) -> int:
        self._to_next_unremoved_stackTop()
        popped_item, popped_id = self.stack.pop()
        self.mutually_removed_id.add(popped_id)
        return popped_item

    def top(self) -> int:
        self._to_next_unremoved_stackTop()
        return self.stack[-1][0]
        
    def _to_next_unremoved_heapTop(self):
        while self.heap and -self.heap[0][1] in self.mutually_removed_id:
            heappop(self.heap)
            
    def popMax(self) -> int:
        self._to_next_unremoved_heapTop()
        popped_item, popped_id = heappop(self.heap)
        self.mutually_removed_id.add(-popped_id)
        return -popped_item 
        
    def peekMax(self) -> int:
        self._to_next_unremoved_heapTop()
        return -self.heap[0][0]


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
```
#### Remark:
- 和min stack的差別主要是在`popMax()`
    - 因為需要達到O(logN), 所以才會聯想到需要多一個heap這樣的資料結構
    - 如果O(N)的話，可以直接用兩個棧就解掉這題
    ```python
    def popMax(self):
        max_number = self.peekMax()
        buffer_stack = []
        while self.top() != max_number:
            buffer_stack.append(self.pop()) # 倒過去
        self.pop() # 這個是主角
        while buffer_stack: # 倒回來
            self.push(buffer_stack[-1])
            buffer_stack.pop()
        return max_number
    ```
#### Submission:
```
Runtime: 547 ms, faster than 97.75% of Python3 online submissions for Max Stack.
Memory Usage: 61.7 MB, less than 54.70% of Python3 online submissions for Max Stack.
```
#### Complexity:
- Time:
  - `push()` O(logN)
  - `pop()` 每個元素最多就被刪兩次，平均O(1)
  - `top()` 同理O(1)
  - `popMax()` 因為heappop O(logN)
  - `peekMax()` 平均O(logN)
- Space: O(N)
