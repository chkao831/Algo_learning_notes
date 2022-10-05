### Maximum Average Subtree
https://leetcode.com/problems/maximum-average-subtree/
>Given the `root` of a binary tree, return the maximum average value of a subtree of that tree.\
>Answers within 10-5 of the actual answer will be accepted.
>
>A subtree of a tree is any node of that tree plus all its descendants.
>
>The average value of a tree is the sum of its values, divided by the number of nodes.
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_avg = -1.0
        self.node_size = 0
    
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        def divideAndConquer(node: TreeNode):
            if not node:
                return (0.0, 0)
            
            left_val, left_size = divideAndConquer(node.left)
            right_val, right_size = divideAndConquer(node.right)
            current_size = left_size + 1 + right_size
            current_avg = (left_val + node.val + right_val)/current_size
            if current_avg > self.max_avg:
                self.max_avg = current_avg
            return (left_val + node.val + right_val, current_size)
        
        divideAndConquer(node=root)
        return self.max_avg
```
#### Remark:
- remember to return `left_val + node.val + right_val` (sum) in the recursive call, not the divided average!!!
- For [Lint597: Subtree with Maximum Average](https://www.lintcode.com/problem/597/), it asks to return the root of the subtree. The only differences lie in
  -  in `__init__`, add attribute `self.max_node = None`
  -  in `divideAndConquer`, when `current_avg > self.max_avg`, add `self.max_node = node`
#### Submission:
```
Runtime: 64 ms, faster than 81.00% of Python3 online submissions for Maximum Average Subtree.
Memory Usage: 17.1 MB, less than 43.80% of Python3 online submissions for Maximum Average Subtree.
```
#### Complexity:
- Time: O(n)
- Space: O(n)
