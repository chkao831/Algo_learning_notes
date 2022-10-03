### Maximum Subtree
https://www.lintcode.com/problem/628/description
> Given a binary tree, find the subtree with maximum sum. Return the `root` of the subtree.
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
        self.curr_max = -1
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
            if curr_weight > self.curr_max or not self.curr_node:
                self.curr_max = curr_weight
                self.curr_node = node
            return curr_weight

        divide_and_conquer(node=root)
        return self.curr_node

```
#### Remark:
- 如果不採取全局變量，可以在`divide_and_conquer()`裡傳`curr_max`和`curr_node`
#### Submission:
```
81 ms
time cost
·
6.12 MB
memory cost
·
Your submission beats
98.00 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(n)
