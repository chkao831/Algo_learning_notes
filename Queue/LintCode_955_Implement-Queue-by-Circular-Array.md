### Implement Queue by Circular Array
https://www.lintcode.com/problem/955/description

<img src="../images/955_Circular-Queue.png" width="700px" />

```python
class CircularQueue:
    def __init__(self, n):
        self.size = 0
        self.queue = [0]*n
        self.head, self.tail = 0, 0
    
    def isFull(self):
        """
        @return:  return true if the array is full
        """
        return self.size == len(self.queue)

    def isEmpty(self):
        """
        @return: return true if there is no element in the array
        """
        return self.size == 0

    def enqueue(self, element):
        """
        @param element: the element given to be added
        @return: nothing
        """
        if self.isFull():
            return
        self.tail = (self.head + self.size) % (len(self.queue))
        self.queue[self.tail] = element
        self.size += 1

    def dequeue(self):
        """
        @return: pop an element from the queue
        """
        if self.isEmpty():
            return -1
        ele = self.queue[self.head]
        self.head = ((self.head + 1) % (len(self.queue)))
        self.size -= 1
        return ele
```

#### Submission:
```
596 ms
time cost
·
6.13 MB
memory cost
·
Your submission beats
51.40 %
Submissions
```
