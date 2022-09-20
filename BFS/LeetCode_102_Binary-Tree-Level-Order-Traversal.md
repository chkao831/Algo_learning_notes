# Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

<img src="../images/102_BFS.jpg" width="300px" />

>Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).\
>Input: `root = [3,9,20,null,null,15,7]`\
>Output: `[[3],[9,20],[15,7]]`

## 單隊列實現方法
In Python the queue implementation with a fast atomic `append()` and `popleft()` is `deque`.

- (a) Initiate queue with a root and start from the level number `0` : `level = 0`.
- While queue is not empty :
  - (b) Start the current level by initiating an empty list of this level.
  - (c) Compute how many elements should be on the current level : it's a queue length.
  - (d) Pop out all these elements from the queue and add them into the current level.
  - (e) Push their child nodes into the queue for the next level.
  - (f) fulfill the current leve, then go to the next level.
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if root is None:
            return levels
        queue = collections.deque([root]) # (a)
        while queue:
            level = [] # (b)
            level_len = len(queue) # (c)
            for _ in range(level_len): 
                node = queue.popleft() # (d')
                level.append(node.val) # (d")
                if node.left:
                    queue.append(node.left) # (e)
                if node.right:
                    queue.append(node.right) # (e)
            levels.append(level) # (f)
        return levels
```
#### Submission:
```
Runtime: 63 ms, faster than 36.74% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.2 MB, less than 84.16% of Python3 online submissions for Binary Tree Level Order Traversal.
```
#### Complexity:
- Time: O(n) since each node is processed exactly once.
- Space: O(n) to keep the output structure which contains n node values.

## 雙隊列實現方法
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        queue: [[3]...]
          ^
          |
        subqueue: [[9, 20]] -- store children
        """
        levels = []
        if root is None:
            return levels
        queue = [root] # (a) Initiate queue with a root and start from the level number 0
        while queue:
            levels.append([node.val for node in queue])  # (b) Append previous level
            sub_queue = [] # (c) Empty up subqueue, store children of the same level
            for node in queue:
                if node.left:
                    sub_queue.append(node.left)
                if node.right:
                    sub_queue.append(node.right)
            queue = sub_queue # (d) Catch children to main queue for next level iteration
        return levels
```
## 鏈表實現方法
