## Minimum Subtree
https://www.lintcode.com/problem/596/
>Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
>The range of input and output data is in int.
### 採用全局變量版
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
        self.minSum = float("inf") # or sys.maxsize
        self.minNode = None

    def find_subtree(self, root: TreeNode) -> TreeNode:
        """
        @param root: the root of binary tree
        @return: the maximum weight node
        """ 

        def divide_and_conquer(node: TreeNode) -> int:
            if not node:
                return 0

            left_val = divide_and_conquer(node.left)
            right_val = divide_and_conquer(node.right)
            curr_sum = left_val + node.val + right_val
            if curr_sum < self.minSum or not self.minNode:
                self.minSum = curr_sum
                self.minNode = node
            return curr_sum

        divide_and_conquer(node=root)
        return self.minNode
```
#### Submission:
```
81 ms
time cost
·
5.98 MB
memory cost
·
Your submission beats
98.40 %
Submissions
```
### 不採用全局變量版 (recommended)
多放了兩個參數進去recursive call
```python
class Solution:

    def find_subtree(self, root: TreeNode) -> TreeNode:
        """
        @param root: the root of binary tree
        @return: the maximum weight node
        """ 

        def divide_and_conquer(node: TreeNode) -> int:
            if not node:
                return 0, float("inf"), None

            left_val, left_minSum, left_minNode = divide_and_conquer(node.left)
            right_val, right_minSum, right_minNode = divide_and_conquer(node.right)
            curr_sum = left_val + node.val + right_val
            if left_minSum == min(left_minSum, curr_sum, right_minSum): # left is optimum
                return (curr_sum, left_minSum, left_minNode)
            elif right_minSum == min(left_minSum, curr_sum, right_minSum): # right is optimum
                return (curr_sum, right_minSum, right_minNode)
            else: # current is still the optimum
                return (curr_sum, curr_sum, node)

        # curr_sum, curr_minSum, curr_minNode
        _, _, curr_minNode = divide_and_conquer(node=root)
        return curr_minNode
```
#### Submission:
```
102 ms
time cost
·
6.15 MB
memory cost
·
Your submission beats
24.20 %
Submissions
```

### Complexity:
- Time: O(n)
- Space: O(n)
