### Odd Even Linked List
https://leetcode.com/problems/odd-even-linked-list/description/

<p>
    <img src="https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg" width="600" />
</p>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        odd_head = odd_tail = head
        even_head = even_tail = head.next
        while even_tail != None and even_tail.next != None:
            odd_tail.next = even_tail.next
            odd_tail = odd_tail.next
            even_tail.next = odd_tail.next
            even_tail = even_tail.next
        odd_tail.next = even_head
        return odd_head
```
#### Remark:
- 永遠讓even_tail走在odd_tail前面，用while loop掌握even_tail及其下一個
#### Submission:
```
Runtime
107 ms
Beats
9.96%

Memory
16.7 MB
Beats
31.62%
```
#### Complexity:
- Time: O(N)
- Space: O(1)
