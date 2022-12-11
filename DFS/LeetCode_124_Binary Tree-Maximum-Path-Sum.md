### Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
>Given the `root` of a binary tree, return the **maximum path sum** of any non-empty path.

<p>
    <img src="https://leetcode.com/problems/binary-tree-maximum-path-sum/solutions/2827786/Figures/124/124_valid_path_examples.png" width="700" />
</p>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.cur_max = -1001

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            subtree_val = left + node.val + right
            depth_val = max(left+node.val, right+node.val, node.val)
            self.cur_max = max(self.cur_max, subtree_val, depth_val)
            return depth_val

        dfs(node=root)
        return self.cur_max
```
#### Remark:
- path sum
  - A path is a continuous sequence of nodes connected to each other. There will always be at least one node in a path. 
  - In a path, except for the starting and ending nodes, every node is connected to two other nodes in the sequence. 
  - These two nodes could either be the node's children, or one of them could be a child, and the other could be the parent node.  
#### Submission:
```
Runtime
88 ms
Beats
94.74%

Memory
21.5 MB
Beats
31.96%
```
#### Complexity:
- Time: O(N)
- Space: O(N)
