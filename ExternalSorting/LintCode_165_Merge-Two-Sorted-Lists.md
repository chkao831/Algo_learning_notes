### Merge Two Sorted Lists
https://www.lintcode.com/problem/165/
>Merge two sorted (ascending) linked lists and return it as a new sorted list. The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.
```python
from lintcode import (
    ListNode,
)

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
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
- Unlike the array version, note that
  - it's `head = tail = ListNode(0)`, don't mistype as `head, tail = ListNode(0)`
  - it's `while l1 and l2`, not `while l1.val and l2.val`
  - at the end, it's `if l1` and `if l2` (just link the remainings), not `while...`, otherwise infinite loop 
#### Submission:
```
103 ms
time cost
·
7.01 MB
memory cost
·
Your submission beats
73.20 %
Submissions
```
#### Complexity:
- Time: O(m+n)
- Space: O(1)
