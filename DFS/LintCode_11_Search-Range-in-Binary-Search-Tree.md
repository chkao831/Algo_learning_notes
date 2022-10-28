### Search Range in Binary Search Tree
https://www.lintcode.com/problem/11/
>Given a binary search tree and a range `[k1, k2]`, return node values within a given range in ascending order.
```python
from typing import (
    List,
)
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    
    def search_range(self, root: TreeNode, k1: int, k2: int) -> List[int]:
        """
        @param root: param root: The root of the binary search tree
        @param k1: An integer
        @param k2: An integer
        @return: return: Return all keys that k1<=key<=k2 in ascending order
        """

        nodes, stack = [], []
        node = root
        while node or stack:
            while node: # go left
                stack.append(node)
                node = node.left
            # exhausted left; retrieve from current stack and go right
            node = stack.pop()
            value = node.val
            if k1 <= value <= k2:
                nodes.append(value)
            if value > k2: # pruning
                break
            node = node.right
        return nodes
```
#### Remark:
- Slightly revised from [中序遍歷](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_94_Binary-Tree-Inorder-Traversal.md)
- 剪枝： `if value > k2: break`
#### Submission:
```
101 ms
time cost
·
8.96 MB
memory cost
·
Your submission beats
97.60 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(n)
