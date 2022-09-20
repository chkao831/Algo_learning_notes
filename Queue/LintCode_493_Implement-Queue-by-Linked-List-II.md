### Implement Queue by Linked List II
https://www.lintcode.com/problem/493/description

```python
class Node():
    def __init__(self, _val):
        self.next, self.prev = None, None
        self.val = _val

class Dequeue(object):

    def __init__(self):
        self.head, self.tail = None, None

    def push_front(self, item):
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            tmp = Node(item)
            self.head.prev = tmp
            tmp.next = self.head
            self.head = tmp

    def push_back(self, item): # enqueue
        if self.tail is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            tmp = Node(item)
            self.tail.next = tmp
            tmp.prev = self.tail
            self.tail = tmp

    def pop_front(self) -> int: # dequeue
        if self.head is not None:
            item = self.head.val
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            return item
        return -1

    def pop_back(self) -> int:
        if self.tail is not None:
            item = self.tail.val
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None
            else:
                self.head = None
            return item
        return -1
```

#### Submission:
```
938 ms
time cost
·
6.12 MB
memory cost
·
Your submission beats
45.60 %
Submissions
```
#### Complexity:
- Time: All with O(1), O(n) for query
