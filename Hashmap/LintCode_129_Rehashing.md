### Rehashing
https://www.lintcode.com/problem/129/description
>
```python
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    

    def addnode(self, newHashTable, number):

        def addlistnode(node, number):
            """
            有隱藏要求，即後到的node要塞到鏈表後面
            """
            while node.next:
                node = node.next
            node.next = ListNode(number)

        newIdx = number % len(newHashTable)
        if newHashTable[newIdx] == None:
            newHashTable[newIdx] = ListNode(number)
        else:
            addlistnode(newHashTable[newIdx], number)

    def rehashing(self, oldHashTable):
        HASH_SIZE = 2 * len(oldHashTable)
        newHashTable = [None for i in range(HASH_SIZE)]
        for item in oldHashTable:
            p = item
            while p != None:
                self.addnode(newHashTable, p.val)
                p = p.next
        return newHashTable
```
#### Remark:
- 
#### Submission:
```
1271 ms
time cost
·
7.11 MB
memory cost
·
Your submission beats
43.00 %
Submissions
```
#### Complexity:
- Time:
- Space:
