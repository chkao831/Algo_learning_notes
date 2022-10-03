## Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/solution/
> Given the `root` of a binary tree, return the inorder traversal of its nodes' values.

<img src="https://leetcode.com/problems/binary-tree-preorder-traversal/Figures/145_transverse.png" />

<img src="https://miro.medium.com/max/640/0*gIonhJjvlBE-SBlv.gif" />

### Recursive Approach

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def inOrder(node: Optional[TreeNode]):
            if not node:
                return
            inOrder(node.left)
            nodes.append(node.val)
            inOrder(node.right)
            
        nodes = []
        inOrder(root)
        return nodes
```
```
Runtime: 42 ms, faster than 74.80% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 14 MB, less than 13.03% of Python3 online submissions for Binary Tree Inorder Traversal.
```
### Iterative Approach with Stack
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes, stack = [], []
        node = root
        while node or stack:
            while node: # go left
                stack.append(node)
                node = node.left
            # exhausted left; retrieve from current stack and go right
            node = stack.pop()
            nodes.append(node.val)
            node = node.right
        return nodes
```
```
Runtime: 32 ms, faster than 93.09% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 14 MB, less than 13.03% of Python3 online submissions for Binary Tree Inorder Traversal.
```
