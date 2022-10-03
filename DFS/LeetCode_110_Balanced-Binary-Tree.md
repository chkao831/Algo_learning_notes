### Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/
>Given a binary tree, determine if it is height-balanced.
>
>For this problem, a height-balanced binary tree is defined as:
>
>**a binary tree in which the left and right subtrees of every node differ in height by no more than 1.**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def divide_and_conquer(node: TreeNode) -> tuple:
            if not node:
                return (True, 0)

            (leftBalanced, leftHeight) = divide_and_conquer(node.left)
            (rightBalanced, rightHeight) = divide_and_conquer(node.right)

            parentHeight = max(leftHeight, rightHeight) + 1
            if (not leftBalanced) or (not rightBalanced) or (abs(leftHeight-rightHeight)>1):
                return (False, parentHeight)
            return (True, parentHeight)
        
        bool_out,_ = divide_and_conquer(node=root)
        return bool_out
```
#### Remark:
- 採用分治法
- The bottom-up algorithm is as follows:
  - Check if the child subtrees are balanced. If they are, use their heights to determine if the current subtree is balanced as well as to calculate the current subtree's height.
#### Submission:
```
Runtime: 100 ms, faster than 41.37% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 19 MB, less than 11.06% of Python3 online submissions for Balanced Binary Tree.
```
#### Complexity:
- Time: O(n)
- Space: O(n) -- The recursion stack may go up to O(n) if the tree is unbalanced.
