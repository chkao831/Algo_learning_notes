### Trim a Binary Search Tree (刪)
https://www.lintcode.com/problem/701/description
<p>
    <img src="http://www.ardendertat.com/wp-content/uploads/2012/01/bst.png" width="500" />
</p>
<p>
    <img src="http://www.ardendertat.com/wp-content/uploads/2012/01/bst_trim.png" width="400" />
</p>

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
    
    def trim_b_s_t(self, root: TreeNode, minimum: int, maximum: int) -> TreeNode:
        """
        @param root: given BST
        @param minimum: the lower limit
        @param maximum: the upper limit
        @return: the root of the new tree 
        """
        
        if not root:
            return None

        if root.val < minimum:
            return self.trim_b_s_t(root.right, minimum, maximum)
        elif root.val > maximum:
            return self.trim_b_s_t(root.left, minimum, maximum)
        else: # minimum <= root <= maximum
            root.left = self.trim_b_s_t(root.left, minimum, maximum)
            root.right = self.trim_b_s_t(root.right, minimum, maximum)
        return root
```
#### Remark:
- 對於原來的BST來說：

  若根節點的值小於最小值，則遞歸調用右子樹並返回右子樹；\
  若根節點的值大於最大值，則遞歸調用左子樹並返回左子樹；\
  否則修剪左子樹、右子樹並返回根節點。
#### Submission:
```
122 ms
time cost
·
10.34 MB
memory cost
·
Your submission beats
22.00 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(n) (遞歸的空間開銷取決於樹的最大深度)
