### Implement Queue by Linked List
https://www.lintcode.com/problem/492/description

```python
class Node():
    def __init__(self, _val):
        self.next = None
        self.val = _val

class MyQueue:
    
    def __init__(self):
        self.head, self.tail = None, None

    def enqueue(self, item):
        """
        @param: item: An integer
        @return: nothing
        """
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next
    
    def dequeue(self):
        """
        @return: An integer
        """
        if self.head is not None:
            item = self.head.val
            self.head = self.head.next
            return item
        return -1
```

#### Submission:
```
1002 ms
time cost
·
21.22 MB
memory cost
·
Your submission beats
29.00 %
Submissions
```
#### Complexity:
- Time: O(1) enqueue; O(1) dequeue; O(n) for query
