## Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
>Given the `root` of a binary tree, return its maximum depth.
>
>A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

### BFS
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        queue = collections.deque([root])
        distance = {root: 1}
        max_distance = 1
        while queue:
            node = queue.popleft()
            if not node.left and not node.right:
                continue
            if node.left:
                queue.append(node.left)
                distance[node.left] = distance[node]+1
                max_distance = max(max_distance, distance[node.left])
            if node.right:
                queue.append(node.right)
                distance[node.right] = distance[node]+1
                max_distance = max(max_distance, distance[node.right])
        return max_distance
```
#### Submission:
```
Runtime: 81 ms, faster than 35.38% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.4 MB, less than 81.09% of Python3 online submissions for Maximum Depth of Binary Tree.
```

## DFS (Warning: more prone to Stack Overflow, compared to BFS)
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def divide_and_conquer(node: TreeNode) -> int:
            if not node:
                return 0
            left_height = divide_and_conquer(node.left)
            right_height = divide_and_conquer(node.right)
            
            return max(left_height, right_height)+1
        
        return divide_and_conquer(node=root)
```
#### Submission:
```
Runtime: 79 ms, faster than 39.27% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.3 MB, less than 23.52% of Python3 online submissions for Maximum Depth of Binary Tree.
```
