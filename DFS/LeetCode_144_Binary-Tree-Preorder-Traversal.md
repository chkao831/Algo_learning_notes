### Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/
> Given the `root` of a binary tree, return the preorder traversal of its nodes' values.

<img src="https://leetcode.com/problems/binary-tree-preorder-traversal/Figures/145_transverse.png" />

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.nodes = []
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        
        self.nodes.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        
        return self.nodes
```

```
   1
 /   \
2     3
 \
  5
  
StdOut: [1, 2, 5, 3]
```

```
       1
     /   \
    2     3
   / \
  4   6
 /
5
  
StdOut: [1, 2, 4, 5, 6, 3]
```
