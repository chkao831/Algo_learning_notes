### Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/
> Given the `root` of a binary tree, return all root-to-leaf paths in any order.
>
>A `leaf` is a node with no children.


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def getPath(node: TreeNode, path: str):
            
            if not node:
                return
            if not node.left and not node.right: # bottom leaf
                paths.append('->'.join([str(node.val) for node in path]))
                return
            
            path.append(node.left)
            getPath(node.left, path)
            path.pop()
            
            path.append(node.right)
            getPath(node.right, path)
            path.pop()
            
        paths = []
        getPath(root, [root])
        return paths
```
#### Remark:
- Mistakes:
  - `if not node.left and not node.right` to be bottom leaf
  - forgot to `return` for bottom leaf
  - need to convert `int` to `str` with `str(node.val)` in contatenation
#### Submission:
```
Runtime: 63 ms, faster than 31.87% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 14 MB, less than 29.71% of Python3 online submissions for Binary Tree Paths.
```
#### Complexity:
- Time: O(N)
- Space: O(N)
