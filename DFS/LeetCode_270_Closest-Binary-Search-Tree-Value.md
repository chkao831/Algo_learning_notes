### Closest Binary Search Tree Value
https://leetcode.com/problems/closest-binary-search-tree-value/
>Given the `root` of a binary search tree and a `target` value, return the value in the BST that is closest to the `target`.
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        def _leftIter(node: TreeNode):
            while node:
                stack.append(node)
                node = node.left
                
        stack = []
        if not root: return stack
        _leftIter(root)
        smaller_closest = float("-inf")
        while stack and stack[-1].val < target:
            node = stack.pop()
            smaller_closest = node.val
            _leftIter(node.right)
        bigger_closest = stack.pop().val if stack else float("inf")
        return smaller_closest if (abs(smaller_closest-target)<=abs(bigger_closest-target)) else bigger_closest
```
#### Remark:
- Based on In Order Traversal (ex. [Lint175](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_95_Validate-Binary-Search-Tree.md)); just that before popping from stack, peek the stack top to see if the value <= target. Pop only when val <= target.
- After retrieving the closest smaller (or equal) value, pop again for the closest bigger value, if available. 
- Followup: [Leet 272 - Closest Binary Search Tree Value II](https://github.com/chkao831/Algo_learning_notes/tree/main/DFS)
#### Submission:
```
Runtime: 87 ms, faster than 23.34% of Python3 online submissions for Closest Binary Search Tree Value.
Memory Usage: 16.1 MB, less than 36.42% of Python3 online submissions for Closest Binary Search Tree Value.
```
#### Complexity:
- Time: O(n)
- Space: O(n)
