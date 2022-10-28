### Search in a Binary Search Tree (查)
https://www.lintcode.com/problem/1524/
>Given the root of a binary search tree (BST) and a `value`.
>
>Return the node whose value equals the given `value`. If such node doesn't exist, return `null`.

查找值為val的節點，如果val小於根節點則在左子樹中查找，反之在右子樹中查找
```python
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    
    def search_b_s_t(self, root: TreeNode, val: int) -> TreeNode:
        """
        @param root: the tree
        @param val: the val which should be find
        @return: the node
        """

        if not root: # if not found
            return None

        if root.val > val:
            return self.search_b_s_t(root=root.left, val=val)
        elif root.val < val:
            return self.search_b_s_t(root=root.right, val=val)
        else: # root.val == val
            return root
```
### Update (改)
修改僅僅需要在查找到需要修改的節點之後，更新這個節點的值就可以了，(假如修改過後整棵樹還滿足BST的性質)
```python
    def update_b_s_t(self, root: TreeNode, target: int, val: int):
        """
        Update the node with value of target to val in BST.
        """

        if not root:
            return # no such target

        if root.val > target:
            update_b_s_t(root=root.left, target=target, val=val)
        elif root.val < target:
            update_b_s_t(root=root.right, target=target, val=val)
        else: # found
            root.val = val # update
```
#### Remark:
- BST的查改
#### Submission:
```
81 ms
time cost
·
6.19 MB
memory cost
·
Your submission beats
99.20 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(n) (遞歸的空間開銷取決於樹的最大深度)
