### Convert Sorted Array to Binary Search Tree
https://www.lintcode.com/problem/1359/description
>Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
>要求二叉搜索樹的高度平衡
```python
from typing import (
    List,
)
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

    def convert_sorted_arrayto_binary_search_tree(self, nums: List[int]) -> TreeNode:
        """
        @param nums: the sorted array
        @return: the root of the tree
        """

        def divide_and_conquer(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            
            mid = (left + right)//2
            cur_root = TreeNode(nums[mid])
            cur_root.left = divide_and_conquer(left=left, right=mid-1)
            cur_root.right = divide_and_conquer(left=mid+1, right=right)
            return cur_root

        return divide_and_conquer(left=0, right=len(nums)-1)
```
#### Remark:
- 以`[-10,-3,0,5,9]`為例
  - 即使要求二叉搜索樹的高度平衡，仍然不可以唯一地確定二叉搜索樹
  
    <p>
      <img src="https://media-lc.lintcode.com/user_476122/202205/698b2a27-313c-45f7-a649-208e81be5f44.png" width="800" />
    </p>

  - 直觀地看，我們可以選擇中間數字作為二叉搜索樹的根節點，這樣分給左右子樹的數字個數相同或只相差1，可以使得樹保持平衡。如果數組長度是奇數，則根節點的選擇是唯一的，如果數組長度是偶數，則可以選擇中間位置左邊的數字作為根節點或者選擇中間位置右邊的數字作為根節點，選擇不同的數字作為根節點則創建的平衡二叉搜索樹也是不同的。
  
    <p>
      <img src="https://media-lc.lintcode.com/user_476122/202205/75e73cda-7440-48b9-a645-714ef8fee445.png" width="500" />
    </p>

  - 決定使用中序遍歷，總是選擇中間位置左邊的數字作為根節點，下標為`mid=(left+right)//2`
 
    <p>
      <img src="https://media-lc.lintcode.com/user_476122/202205/97d91ba8-c3d1-4422-bc0e-4b4b4b0d47bb.png" width="650" />
    </p>

- 記住左子樹起點=`left`, 右子樹起點=`mid+1`(不是`mid`), 右子樹終點=`right`
  ```python
  cur_root.left = divide_and_conquer(left=left, right=mid-1)
  cur_root.right = divide_and_conquer(left=mid+1, right=right)
  ```
#### Submission:
```
102 ms
时间消耗
·
8.70 MB
空间消耗
·
您的提交打败了
95.00 %
的提交
```
#### Complexity:
- Time: O(n)
- Space: 遞歸棧的深度是O(logn)
