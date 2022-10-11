## Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/
> Given the `root` of a binary tree, return the preorder traversal of its nodes' values.

<img src="https://leetcode.com/problems/binary-tree-preorder-traversal/Figures/145_transverse.png" />

<img src="https://miro.medium.com/max/640/0*PaTE01wN4ToA40Co.gif" />

### Recursive Approach

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
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        
        self.nodes.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        
        return self.nodes
```
In 1-line:
```python
def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []
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
    
    def __init__(self):
        self.nodes = []
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return self.nodes
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                self.nodes.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left) # LIFO
        
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
