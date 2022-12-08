# Merge K Sorted Lists
https://www.lintcode.com/problem/104/description
>

## 1. Heap

```python
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

## 1. Heap

# overwrite the compare function 
# so that we can directly put ListNode into heapq
ListNode.__lt__ = lambda x, y: (x.val < y.val)

from heapq import heappush, heappop

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        dummy = tail = ListNode(0)
        heap = []
        for head in lists:
            if head:
                heappush(heap, head)
                
        while heap:
            head = heappop(heap)
            tail.next = head
            tail = head
            if head.next:
                heappush(heap, head.next)
                    
        return dummy.next
```
#### Remark:
- mistake: tuple比较的时候，如果（node1.val, node1）和（node2.val,node2）同时存在，heap在计算最小值的时候需要比较，如果node1.val和node2.val一样，那么node1和node2就需要比较，但这两个Listnode不支持比较。
#### Submission:
```
1167 ms
time cost
·
8.96 MB
memory cost
·
Your submission beats
13.80 %
Submissions
```
#### Complexity:
- Time:
- Space:

## 2. 兩兩歸併

```python
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


### 2. Pairing -> Merge

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists:
            return None

        while len(lists) > 1:
            merged_combo = []
            for i in range(0, len(lists), 2):
                merged = []
                if (i+1) == len(lists):
                    merged = lists[i]
                else:
                    merged = self.merge_two_lists(l1=lists[i], l2=lists[i+1])
                merged_combo.append(merged)
            lists = merged_combo
        return lists[0]

    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = tail = ListNode(0) # dummy head
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return head.next
```
#### Remark:
- `while len(lists) > 1`, not `if len(lists) > 1`
- `return lists[0]`, not `return lists`
- 用兩倆歸併的方法 二叉樹的形式
每個數最多參與logK次的歸併
總共N個數 => O(NlogK)
#### Submission:
```
1083 ms
time cost
·
8.89 MB
memory cost
·
Your submission beats
61.20 %
Submissions
```
#### Complexity:
- Time:
- Space:

## 3. Merge sort, Divide and Conquer

```python
from typing import List

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists: List):
        if not lists:
            return None
        return self.divide_and_conquer(lists=lists, start=0, end=len(lists)-1)

    def divide_and_conquer(self, lists: List, start: int, end: int) -> ListNode:
        if start >= end:
            return lists[start]
        mid = (start+end)//2
        left = self.divide_and_conquer(lists=lists, start=start, end=mid)
        right = self.divide_and_conquer(lists=lists, start=mid+1, end=end)
        return self.merge_two_lists(l1=left, l2=right)

    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
    
        head = tail = ListNode(0) # dummy head
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return head.next
```
#### Remark:
- `if l1`, `if l2`, not `while`
- `head = tail = ListNode(0)`
- `while l1 and l2`, not `while l1.val and l2.val`
#### Submission:
```
1046 ms
time cost
·
8.86 MB
memory cost
·
Your submission beats
83.80 %
Submissions
```
#### Complexity:
- Time:
- Space:
