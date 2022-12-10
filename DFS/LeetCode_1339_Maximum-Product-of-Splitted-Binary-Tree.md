### Maximum Product of Splitted Binary Tree
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/
>Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.
>
>Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo `10^9 + 7`.

<p>
    <img src="https://assets.leetcode.com/uploads/2020/01/21/sample_1_1699.png" width="600" />
</p>

1. Calculate the sum of the entire tree.
2. Check the product we'd get for each subtree.
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:

    def __init__(self):
        self.total_sum = 0
        self.current_best_prod = 0

    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def _total_sum(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            queue = deque([root])
            sum_out = 0
            while queue:
                node = queue.popleft()
                sum_out += node.val
                if node.left or node.right:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return sum_out
        
        def _dfs(node: TreeNode) -> int:
            if not node:
                return 0
            left_val = _dfs(node.left)
            right_val = _dfs(node.right)
            current_sum = left_val + node.val + right_val
            remain_sum = self.total_sum - current_sum
            self.current_best_prod = max(self.current_best_prod, current_sum*remain_sum)
            return current_sum

        self.total_sum = _total_sum(root)
        _dfs(root)
        return self.current_best_prod % (10**9+7)
```
#### Remark:
- 注意遞歸函數到底要吃什麼＋回傳什麼
  - 吃當前的node: 算加上當前的node, 值是多少
  - 向上回傳直到當前的sum: 然後慢慢算上去
  - `current_best_prod`採全局變量 
#### Submission:
```
Runtime
559 ms
Beats
69.16%

Memory
74.8 MB
Beats
77.58%
```
#### Complexity:
- Time: O(n)
- Space: O(n) in worst case, if tree is not balanced.
