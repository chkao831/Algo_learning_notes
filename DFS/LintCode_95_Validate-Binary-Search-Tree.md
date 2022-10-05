### Validate Binary Search Tree
https://www.lintcode.com/problem/95/description
>Given a binary tree, determine if it is a valid binary search tree (BST).
>Note that in this problem, the left subtree of a node contains only nodes with keys **less than** the node's key; The right subtree of a node contains only nodes with keys **greater than** the node's key.
```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    
    def isValidBST(self, root):
        """
        @param root: The root of binary tree.
        @return: True if the binary tree is BST, or false
        """

        def leftIter(node):
            while node:
                stack.append(node)
                node = node.left

        if not root:
            return True

        node, stack = root, []
        leftIter(node)
        while stack:
            last_left = curr_node = stack.pop()
            if curr_node.right:
                leftIter(curr_node.right)
            # slightly differs from inOrderTraversal as this problem disallowed equal values
            if stack:
                if stack[-1].val <= last_left.val: # so it's <= not <
                    return False
        return True
```
#### Remark:
- Revised from [Binary Search Tree Iterator](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_173_Binary-Search-Tree-Iterator.md)
- To peek the stack top: `stack[-1].val`; to pop the stack top: `stack.pop()`
#### Submission:
```
122 ms
time cost
·
10.98 MB
memory cost
·
Your submission beats
87.40 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(h) ~O(n)
