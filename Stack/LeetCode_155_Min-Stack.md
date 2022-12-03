# Min Stack
https://leetcode.com/problems/min-stack/
>Design a stack that supports push, pop, top, and retrieving the minimum element **in constant time**.
>
>Implement the `MinStack` class:
>
>`MinStack()` initializes the stack object.\
>`void push(int val)` pushes the element val onto the stack.\
>`void pop()` removes the element on the top of the stack.\
>`int top()` gets the top element of the stack.\
>`int getMin()` retrieves the minimum element in the stack.\
You must implement a **solution with O(1) time complexity for each function**.



## 平行min_tracker
```
self.stack =         [4, 2, 3, 1, 1, 2, 3]
self.stack_tracker = [4, 2, 2, 1, 1, 1, 1]
```
```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_tracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        tracker_num = val if (not self.stack_tracker or val < self.stack_tracker[-1]) else self.stack_tracker[-1]
        self.stack_tracker.append(tracker_num)

    def pop(self) -> None:
        self.stack.pop()
        self.stack_tracker.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_tracker[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
#### Remark:
- 
#### Submission:
```
Runtime: 125 ms, faster than 57.83% of Python3 online submissions for Min Stack.
Memory Usage: 18.2 MB, less than 32.64% of Python3 online submissions for Min Stack.
```

## 優化空間版
```
self.stack =         [4, 2, 3, 1, 1, 2, 3]
self.stack_tracker = [4, 2,    1, 1      ]
```
```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_tracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack_tracker or val <= self.stack_tracker[-1]:
            self.stack_tracker.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.stack_tracker[-1]:
            self.stack_tracker.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_tracker[-1]
```
#### Remark:
- 
#### Submission:
```
Runtime: 61 ms, faster than 94.45% of Python3 online submissions for Min Stack.
Memory Usage: 17.8 MB, less than 77.77% of Python3 online submissions for Min Stack.
```

## 更優化空間by計數版
```
self.stack =         [ 4,    2,   3, 1, 1, 2, 3]
self.stack_tracker = [[4,1],[2,1],  [1,2]
```
```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_tracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack_tracker or val < self.stack_tracker[-1][0]:
            self.stack_tracker.append([val, 1])
            return
        if val == self.stack_tracker[-1][0]:
            self.stack_tracker[-1][1] += 1

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.stack_tracker[-1][0]:
            self.stack_tracker[-1][1] -= 1
        if self.stack_tracker[-1][1] == 0:
            self.stack_tracker.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_tracker[-1][0]
```
#### Remark:
- 忘記tracker計數減成零時，把該項刪掉了
  ```
  if self.stack_tracker[-1][1] == 0:
      self.stack_tracker.pop()
  ```
- 相對前兩版，更優化，但是較難implement  
#### Submission:
```
Runtime: 59 ms, faster than 96.19% of Python3 online submissions for Min Stack.
Memory Usage: 17.8 MB, less than 96.16% of Python3 online submissions for Min Stack.
```

## Complexity
- Time:
  - `push()`: O(1)
  - `pop()`: O(1)
  - `top()`: O(1)
  - `getMin()`: O(1)
- Space: O(n)
