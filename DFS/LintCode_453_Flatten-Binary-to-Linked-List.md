### Flatten Binary Tree to Linked List
https://www.lintcode.com/problem/453/
> Flatten a binary tree to a fake "linked list" in pre-order traversal.
>
>Here we use the right pointer in TreeNode as the next pointer in ListNode.

- Pre-order: 根 -> 左 -> 右
  -  所以，一棵樹被攤平後，返回這棵樹的最尾部節點時，順序就是右 -> 左 -> 根
  -  要返回這棵樹的最尾部節點的原因是**要知道這個被攤平的鏈表尾巴在哪裡**，要左右兩端連接的時候才可以定位
- 樹的鏈表 ＝ 樹的根節點 ＋ 左子樹鏈表 ＋ 右子樹鏈表
- Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.
![](../images/453_FlattenBT.jpg)

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
    
    def flatten(self, root: TreeNode):
        """
        @param root: a TreeNode, the root of the binary tree
        @return: nothing
        """

        if not root:
            return None
        
        last_left = self.flatten(root.left)
        last_right = self.flatten(root.right)
        if last_left:
            last_left.right = root.right
            root.right = root.left
            root.left = None
        return last_right or last_left or root
```
#### Remark:
- 
#### Submission:
```
101 ms
time cost
·
6.78 MB
memory cost
·
Your submission beats
68.80 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(n)
