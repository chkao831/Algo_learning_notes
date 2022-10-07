### Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
>Given the `root` of a binary search tree, and an integer `k`, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def leftIter(node):
            while node:
                stack.append(node)
                node = node.left
        
        if not root:
            return None
        count, stack, returned_val = 1, [], None
        leftIter(root)
        while stack and count <= k:
            node = stack.pop()
            leftIter(node.right)
            returned_val = node.val # for this stack pop
            count += 1 # for this stack pop
        return returned_val
```
#### Remark:
- Structurally similar to [Lint 95 - Validate Binary Search Tree](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_95_Validate-Binary-Search-Tree.md)
#### Submission:
```
Runtime: 100 ms, faster than 40.86% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18 MB, less than 88.58% of Python3 online submissions for Kth Smallest Element in a BST.
```
#### Complexity:
- Time: O(max(k,h)) (or simply O(n))
  - This complexity is defined by the stack, which contains at least k+h element; O(k+h) = O(max(k,h))
- Space: O(h) to keep the stack (O(n) worst case)

#### Potential Followup: 
Q: 二叉樹（節點）經常被修改，如何優化？\
A: 在TreeNode中增加一個counter, 代表該節點的節點個數，在被修改的過程中不斷修正受影響的TreeNode的資訊。用類似Quick Select的算法去二分找到kth smallest.

As a reference, 本題用Quick Select也可以解 (followup只是把`count()`這個recursive call變成一個counter去紀錄，方便後續查找）
```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def count(root):
            if not root: 
                return 0
            return 1 + count(root.left) + count(root.right)
        
        n_left = count(root.left)
        if n_left == k - 1: 
            return root.val
        elif n_left < k - 1: # 左半部分不夠k，剩下去右半找
            return self.kthSmallest(root.right, k - n_left - 1)
        else: 
            return self.kthSmallest(root.left, k)
```
O(h) Time Complexity (at each partition time, choose **either side** to proceed; not both.)
