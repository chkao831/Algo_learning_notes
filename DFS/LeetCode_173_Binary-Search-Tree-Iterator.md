## Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/
>Implement the BSTIterator class that represents an iterator over the **in-order traversal** of a binary search tree (BST).

### Method 1: 先進行完整中序遍歷，然後從結果取next
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        self.curr_idx = -1
        self._inOrder(root=root)

    def next(self) -> int:
        self.curr_idx += 1
        return self.nodes[self.curr_idx]

    def hasNext(self) -> bool:
        return self.curr_idx + 1 < len(self.nodes)
        
    def _inOrder(self, root: TreeNode):
        stack, node = [], root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            self.nodes.append(node.val)
            node = node.right
            
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```
#### Submission:
```
Runtime: 175 ms, faster than 15.57% of Python3 online submissions for Binary Search Tree Iterator.
Memory Usage: 20.1 MB, less than 70.45% of Python3 online submissions for Binary Search Tree Iterator.
```
#### Complexity:
- Time: O(n) taken by the constructor for the iterator; O(1) for `next()` and `hasNext()`.
- Space: O(n)

### Method 2: 寫一個往左走的helper，棧非空就有下一個節點可以取＋其右子樹可以遍歷
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._leftIter(root=root)

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self._leftIter(node.right)
        return node.val
    
    def hasNext(self) -> bool:
        return bool(self.stack)
        
    def _leftIter(self, root):
        node = root
        while node:
            self.stack.append(node)
            node = node.left
```
#### Submission:
```
Runtime: 123 ms, faster than 57.71% of Python3 online submissions for Binary Search Tree Iterator.
Memory Usage: 20.5 MB, less than 13.22% of Python3 online submissions for Binary Search Tree Iterator.
```
#### Complexity:
- Time: O(n) for `next()` (O(1) to `pop`, but O(n) in the worst case to do `_leftIter()`); O(1) for `hasNext()`
- Space: O(n)
