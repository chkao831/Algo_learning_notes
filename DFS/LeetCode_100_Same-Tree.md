### Same Tree
https://leetcode.com/problems/same-tree/description/
>Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
>
>Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
```python
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        if not p and not q:
            return True
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
```
#### Submission:
```
Runtime
32 ms
Beats
84.20%

Memory
13.9 MB
Beats
27.10%
```
#### Complexity:
- Time: O(N)
- Space: O(N) in worst case, where the tree is unbalanced (depth of N)
