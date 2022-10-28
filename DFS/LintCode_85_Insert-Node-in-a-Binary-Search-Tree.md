### Insert Node in a Binary Search Tree (增)
https://www.lintcode.com/problem/85/description
>Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.
```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:

    def insertNode(self, root, node):
        """
        @param: root: The root of the binary search tree.
        @param: node: insert this node into the binary search tree
        @return: The root of the new binary search tree.

        在樹上定位要插入節點的位置。

        如果它大於當前根節點，則應該在右子樹中，
        如果它小於當前根節點，則應該在左子樹中。
        （二叉查找樹中保證不插入已經存在的值）
        """

        if not root:
            return node # 到葉子節點了（是時候插入了），給要插的點

        if root.val > node.val:
            root.left = self.insertNode(root=root.left, node=node)
        else: # root.val <= node.val
            root.right = self.insertNode(root=root.right, node=node)
        return root # return the tree in the last return

```
#### Remark:
- 
#### Submission:
```
896 ms
时间消耗
·
8.92 MB
空间消耗
·
您的提交打败了
96.00 %
的提交
```
#### Complexity:
- Time: O(n)
- Space: O(1)
