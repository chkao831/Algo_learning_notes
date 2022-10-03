## Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/
> Given the `root` of a binary tree, return the postorder traversal of its nodes' values.

<img src="https://leetcode.com/problems/binary-tree-preorder-traversal/Figures/145_transverse.png" />

<img src="https://miro.medium.com/max/640/0*najybdVtx7wCsu_u.gif" />

### Recursive Approach
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def postOrder(node: Optional[TreeNode]):
            if not node:
                return
            postOrder(node.left)
            postOrder(node.right)
            nodes.append(node.val)
            
        nodes = []
        postOrder(root)
        return nodes
```
```
Runtime: 58 ms, faster than 32.68% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 13.9 MB, less than 13.33% of Python3 online submissions for Binary Tree Postorder Traversal.
```
In 1-line:
```python
def postorder(root):
    return  postorder(root.left) + postorder(root.right) + [root.val] if root else []
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        nodes, stack = [], []
        node = root
        while stack or node:
            while node:
                nodes.append(node.val)
                stack.append(node)
                node = node.right
            node = stack.pop().left
        print(nodes)
        return nodes[::-1]
```
```
Runtime: 60 ms, faster than 26.51% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 13.9 MB, less than 13.33% of Python3 online submissions for Binary Tree Postorder Traversal.
```
