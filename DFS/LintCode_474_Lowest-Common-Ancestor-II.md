## Lowest Common Ancestor II
https://www.lintcode.com/problem/474/
>給一棵二叉樹和二叉樹中的兩個節點，找到這兩個節點的最近公共祖先LCA。
>
>兩個節點的最近公共祖先，是指兩個節點的所有父親節點中（包括這兩個節點），離這兩個節點最近的公共的節點。
>
>每個節點除了左右兒子指針以外，**還包含一個父親指針parent**，指向自己的父親。

### 方法: 使用哈希表紀錄從A到root的所有點（包括自己），訪問從B到root的所有點，第一個出現的就是。
```python
"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""

class Solution:
    
    def lowestCommonAncestorII(self, root, A, B):
        """
        @param: root: The root of the tree
        @param: A: node in the tree
        @param: B: node in the tree
        @return: The lowest common ancestor of A and B
        """

        def addParent(node: "ParentTreeNode"):
            while node: # includes A itself
                set_A.add(node)
                node = node.parent

        def inspectParent(node: "ParentTreeNode") -> ParentTreeNode:
            while node: # includes B itself
                if node in set_A:
                    return node
                node = node.parent
            return None

        set_A = set()
        addParent(A)
        return inspectParent(B)

```
#### Remark:
- 這題給了一個父指針，用到父指針才是最優解
#### Submission:
```
1178 ms
time cost
·
12.54 MB
memory cost
·
Your submission beats
5.40 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(h) ~O(n)
