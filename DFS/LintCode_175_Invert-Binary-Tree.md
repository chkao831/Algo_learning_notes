## Invert Binary Tree
https://www.lintcode.com/problem/175/description
> Invert a binary tree.Left and right subtrees exchange.

### BFS: Iterative Approach
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
    
    def invert_binary_tree(self, root: TreeNode):
        """
        @param root: a TreeNode, the root of the binary tree
        @return: nothing
        """
        if not root:
            return
        queue = collections.deque([root])
        while queue:
            node = queue.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
```
#### Submission:
```
206 ms
time cost
·
13.15 MB
memory cost
·
Your submission beats
3.60 %
Submissions
```
#### Complexity:
- Time: O(n) 每個節點都需要入隊列/出隊列一次
- Space: O(n) 最壞的情況下會包含所有的葉子節點，完全二叉樹葉子節點是 n/2個，所以時間複雜度是 O(n)

### DFS: Recursive Approach
```python
class Solution:
    
    def invert_binary_tree(self, root: TreeNode):
        """
        @param root: a TreeNode, the root of the binary tree
        @return: nothing
        """

        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invert_binary_tree(root.left)
        self.invert_binary_tree(root.right)
```
#### Submission:
```
122 ms
time cost
·
9.21 MB
memory cost
·
Your submission beats
10.60 %
Submissions
```
#### Complexity:
- Time: O(n) 會遍歷二叉樹中的每一個節點
- Space: O(h) ~O(n) 由遞歸深度決定
