### Maximum Difference Between Node and Ancestor
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/
>Given the `root` of a binary tree, find the maximum value `v` for which there exist different nodes `a` and `b` where `v = |a.val - b.val|` and `a` is an ancestor of `b`.


初版
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs (node: TreeNode, cur_max_val: float, cur_min_val: float) -> Tuple[TreeNode, float, float]:
            if not node:
                return (None, cur_max_val, cur_min_val)
            cur_max_val = max(node.val, cur_max_val)
            cur_min_val = min(node.val, cur_min_val)
            left_node, left_max, left_min = dfs(node.left, cur_max_val, cur_min_val)
            right_node, right_max, right_min = dfs(node.right, cur_max_val, cur_min_val)

            return (None, left_max, left_min) if abs(left_max-left_min)>abs(right_max-right_min) else (None, right_max, right_min)
            
        _, out_max, out_min = dfs(node=root, cur_max_val=-1, cur_min_val=10**5+1)
        return abs(out_max-out_min)

```
#### Submission:
```
Runtime
37 ms
Beats
97.32%

Memory
20.3 MB
Beats
13.84%
```

修改：
- dfs的返回值不需要有node本身
```python
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs (node: TreeNode, cur_max_val: float, cur_min_val: float) -> Tuple[float, float]:
            if not node:
                return (cur_max_val, cur_min_val)
            cur_max_val = max(node.val, cur_max_val)
            cur_min_val = min(node.val, cur_min_val)
            left_max, left_min = dfs(node.left, cur_max_val, cur_min_val)
            right_max, right_min = dfs(node.right, cur_max_val, cur_min_val)

            return (left_max, left_min) if abs(left_max-left_min)>abs(right_max-right_min) else (right_max, right_min)
            
        out_max, out_min = dfs(node=root, cur_max_val=-1, cur_min_val=10**5+1)
        return abs(out_max-out_min)
```
#### Submission:
```
Runtime
52 ms
Beats
77.85%

Memory
19.9 MB
Beats
91.9%
```
- 再者，可以在base case返回時就減好absolute value，當作返回值return，不要受到dfs input是什麼影響
```python
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs (node: TreeNode, cur_max_val: float, cur_min_val: float) -> float:
            if not node:
                return abs(cur_max_val-cur_min_val)
            cur_max_val = max(node.val, cur_max_val)
            cur_min_val = min(node.val, cur_min_val)
            left_max_abs = dfs(node.left, cur_max_val, cur_min_val)
            right_max_abs = dfs(node.right, cur_max_val, cur_min_val)

            return (max(left_max_abs, right_max_abs))
            
        out = dfs(node=root, cur_max_val=-1, cur_min_val=10**5+1)
        return out
```
#### Submission:
```
Runtime
46 ms
Beats
85.64%

Memory
19.9 MB
Beats
91.9%
```

#### Remark:
- 關鍵就是想清楚一棵樹下去的時候，在呼叫遞歸前要先記好目前的至此的最大最小，然後從底部開始返還最大絕對值

#### Complexity:
- Time: O(n)
- Space: O(n)
