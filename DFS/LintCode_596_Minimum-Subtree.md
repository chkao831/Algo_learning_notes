### Minimum Subtree
https://www.lintcode.com/problem/596/
>Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
>The range of input and output data is in int.
```python
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

    def __init__(self):
        self.curr_min = float("inf")
        self.curr_node = None

    def find_subtree(self, root: TreeNode) -> TreeNode:
        """
        @param root: the root of binary tree
        @return: the maximum weight node
        """ 

        def divide_and_conquer(node: TreeNode) -> int:
            if not node:
                return 0

            left_weight = divide_and_conquer(node.left)
            right_weight = divide_and_conquer(node.right)
            curr_weight = left_weight + node.val + right_weight
            if curr_weight < self.curr_min or not self.curr_node:
                self.curr_min = curr_weight
                self.curr_node = node
            return curr_weight

        divide_and_conquer(node=root)
        return self.curr_node
```
#### Remark:
- 
#### Submission:
```
102 ms
time cost
·
6.16 MB
memory cost
·
Your submission beats
24.20 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(n)
