### Partition List
https://leetcode.com/problems/partition-list/
>Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
>
>You should preserve the original relative order of the nodes in each of the two partitions.

<img src="../images/86_Partition_List.png" width="600px" />

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        """
        (1) former_dummy -> null
        (2) latter_dummy -> null
        """
        former = former_dummy = ListNode(0)
        latter = latter_dummy = ListNode(0)
        
        while head:
            '''
            (3) make sure curr.next is captured
            (4) link current tail
            (5) link current head
            (6) move (shift) to next
            '''
            curr_next = head.next              # (3)
            if head.val < x:
                # head.next = former.next        # (4) link tail to null, can be skipped
                former.next = head             # (5)
                former = former.next           # (6)
            else: # head.val >= x 
                head.next = latter.next        # (4) link tail to null
                latter.next = head             # (5)
                latter = latter.next           # (6)
            head = curr_next                   # (6')
        
        former.next = latter_dummy.next
        
        return former_dummy.next
        
```
#### Remark:
- Remember `latter.next = None`, since the last node of "after" list would also be ending node of the reformed list. 
#### Submission:
```
Runtime: 1927 ms, faster than 5.59% of Python3 online submissions for Partition List.
Memory Usage: 14.4 MB, less than 29.00% of Python3 online submissions for Partition List.
```
#### Complexity:
- Time: O(n)
- Space: O(1)
