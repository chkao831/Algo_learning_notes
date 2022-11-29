### First Unique Number
https://leetcode.com/problems/first-unique-number/

>Implement the `FirstUnique` class:
>
>`FirstUnique(int[] nums)` Initializes the object with the numbers in the queue.\
>`int showFirstUnique()` returns the value of the first unique integer of the queue, and returns `-1` if there is no such integer.\
>`void add(int value)` insert value to the queue.

- Offline Algorithm (離線算法) version: [Lint685 - First Unique Number in Data Stream](https://github.com/chkao831/Algo_learning_notes/blob/main/Queue/LintCode_685_First-Unique-Number-in-Data-Stream.md) FIFO with queue. High time complexity. 

```python
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dict_valToPrevNode= {}
        self.set_duplicates = set()
        self.dummy = ListNode(0)
        self.tail = self.dummy
        
        for num in nums:
            self.add(value=num)

    def showFirstUnique(self) -> int:
        if not self.dummy.next:
            return -1
        else:
            return self.dummy.next.val

    def add(self, value: int) -> None:
        
        def _pushback(val: int):
            newNode = ListNode(val)
            # to-next
            old_tail = self.tail
            old_tail.next = newNode
            self.tail = newNode
            # to-prev
            self.dict_valToPrevNode[val] = old_tail
            
        def _remove(val: int):
            prev = self.dict_valToPrevNode[val]
            curr = prev.next
            del self.dict_valToPrevNode[val]

            if curr is self.tail:
                self.tail = prev
                prev.next = None
            else:
                prev.next = curr.next
                self.dict_valToPrevNode[curr.next.val] = prev
        
        # case1: appeared 3+ times, do nothing
        if value in self.set_duplicates:
            pass
        # case2: appeared twice, remove
        elif value in self.dict_valToPrevNode:
            _remove(val=value)
            self.set_duplicates.add(value)
        # case3: never appeared, add
        else:
            _pushback(val=value)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
```
#### Remark:
- Definition of ListNote class in LeetCode:
```python
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
```
#### Submission:
```
Runtime: 1153 ms, faster than 76.36% of Python3 online submissions for First Unique Number.
Memory Usage: 84.6 MB, less than 14.32% of Python3 online submissions for First Unique Number.
```
#### Complexity:
- Time: O(K) for constructor (K calls to `add()`); O(1) for others
- Space: O(N)
