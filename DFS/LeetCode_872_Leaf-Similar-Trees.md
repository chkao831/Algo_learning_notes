### Leaf-Similar Trees
https://leetcode.com/problems/leaf-similar-trees/description/
>Two binary trees are considered leaf-similar if their leaf value sequence is the same.
>
>Return `true` if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, node: TreeNode, list_out: List):
        # base case
        if not node:
            return
        if not node.left and not node.right:
            list_out.append(node.val)
        # recursive case
        self.dfs(node=node.left, list_out=list_out)
        self.dfs(node=node.right, list_out=list_out)
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        list_out_1, list_out_2 = [], []
        self.dfs(node=root1, list_out=list_out_1)
        self.dfs(node=root2, list_out=list_out_2)
        return list_out_1 == list_out_2
    
```
#### Remark:
- Forgot `if not node: return`, resulting in having `None.left` and `None.right`
#### Submission:
```
Runtime
62 ms
Beats
48.38%

Memory
13.9 MB
Beats
46.25%
```
#### Complexity:
- Time: O(n)
- Space: O(n) worst, if unbalanced
