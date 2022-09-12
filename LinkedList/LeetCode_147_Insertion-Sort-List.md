### Insertion Sort List
https://leetcode.com/problems/insertion-sort-list/
>Given the `head` of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
>
>The steps of the insertion sort algorithm:
>
>Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.\
>At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.\
>It repeats until no input elements remain.\
>The following is a graphical example of the insertion sort algorithm. The partially sorted list initially contains only the first element in the list. One element is removed from the input data and inserted in-place into the sorted list with each iteration.
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        dummy -> null | 4  2  1  3 -> null
        <prev>         <c><n>
        
        dummy -> 4 - > null | 2  1  3 -> null
        
        while curr:
            (1) always get the prev back to dummy
            (2) iterate through dummy.next and compare with current value
            Found position, ready to unlink + link:
            (3) make sure curr.next is assigned
            (4) link curr tail
            (5) link curr head
            (6) move to the next unsorted position
        """
        dummy = ListNode()
        curr = head
        
        while curr:
            prev = dummy                                  #(1)
            while prev.next and prev.next.val < curr.val: #(2)
                prev = prev.next                      
            # found position
            cur_next = curr.next                          #(3)
            curr.next = prev.next                         #(4)
            prev.next = curr                              #(5)
            curr = cur_next                               #(6)
        return dummy.next
```
#### Remark:
- miswrote `prev.next.val < curr.val` as prev.next < curr.val
#### Submission:
```
Runtime: 1677 ms, faster than 48.46% of Python3 online submissions for Insertion Sort List.
Memory Usage: 16.5 MB, less than 83.76% of Python3 online submissions for Insertion Sort List.
```
#### Complexity:
- Time: O(n^2)
- Space: O(1)
