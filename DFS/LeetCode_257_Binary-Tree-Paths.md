## Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/
> Given the `root` of a binary tree, return all root-to-leaf paths in any order.
>
>A `leaf` is a node with no children.

<img src="https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg" />

### Recursive Approach: DFS (Postorder Traversal), with Manual Backtracking
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def getPath(node: TreeNode, path: str):
            
            if not node:
                return
            if not node.left and not node.right: # bottom leaf
                paths.append('->'.join([str(node.val) for node in path]))
                return
            
            path.append(node.left)
            getPath(node.left, path)
            path.pop()
            
            path.append(node.right)
            getPath(node.right, path)
            path.pop()
            
        paths = []
        getPath(root, [root])
        return paths
```

- Another less-intuitive approach without Manual Backtracking (but suboptimal for string concatenation)
    ```python

    class Solution:
        def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

            paths = []
            if not root:
                return []
            if not root.left and not root.right:
                return [str(root.val)] # ['5']

            for path in self.binaryTreePaths(root.left):
                paths.append(str(root.val) + '->' + path)
            for path in self.binaryTreePaths(root.right):
                paths.append(str(root.val) + '->' + path) # ['2->5']

            return paths
    ```
#### Remark:
- Mistakes:
  - `if not node.left and not node.right` to be bottom leaf
  - forgot to `return` for bottom leaf
  - need to convert `int` to `str` with `str(node.val)` in contatenation
#### Submission:
```
Runtime: 63 ms, faster than 31.87% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 14 MB, less than 29.71% of Python3 online submissions for Binary Tree Paths.
```
### Iterative Approach
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        if not root:
            return []
        
        paths, stack_nodeAndPathstr = [], [(root, str(root.val))]
        while stack_nodeAndPathstr:
            node, path = stack_nodeAndPathstr.pop()
            if not node.left and not node.right:
                paths.append(path)
                continue
            if node.left:
                stack_nodeAndPathstr.append((node.left, "->".join([path, str(node.left.val)])))
            if node.right:
                stack_nodeAndPathstr.append((node.right, "->".join([path, str(node.right.val)])))
        return paths
```
#### Remark:
- need to append as string format to path, since there's no backtracking in iterative approaches
    - However, do note that `path += '->'` is bad because this will create a lot of useless strings in the heap. 
- To append more than one element to stack, remember `[( , )]` the brackets.
- Output order is slightly different from the recursive approach:
    ```
    Accepted
        Runtime: 59 ms
        Your input
        [1,2,3,null,5]
        Output
        ["1->3","1->2->5"]
        Diff
        Expected
        ["1->2->5","1->3"]
    ```
#### Submission:
```
Runtime: 63 ms, faster than 31.87% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 14 MB, less than 29.71% of Python3 online submissions for Binary Tree Paths.
```

### Complexity:
- Time: O(N)
- Space: O(N)
