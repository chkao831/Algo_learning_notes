## Serialize and Deserialize Binary Tree
https://www.lintcode.com/problem/7/
> Design an algorithm and write code to serialize and deserialize a binary tree.

### 序列化 與 反序列化
- 序列化：將內存中結構化的數據變成字符串的過程
  - Serialize: object to string
  - Deserialize: string to object
- 為何需要序列化？
  - 將內存中的數據持久話存儲時
    - 重要的內存需要寫入硬盤，需要時再從硬盤中讀出來在內存中
  - 網絡傳輸時
    - 機器間交換數據時不讀內存，而是將數據變成字符流數據
- 常見的序列化：XML, Json, Thrift (Facebook), ProtoBuf (Google)     
  - 數組
    - `"[1, 2, 3]"`
  - 整數鏈表
    - `"1 -> 2 -> 3"`
  - 哈希表
    - `"{\"key\":}\"value\"}"` 
- 需要考慮的因素
  - 壓縮率
  - 可讀性
### 二叉樹的序列化
We represent binary tree in BFS order.
```python
  1
 / \
2   3
```
the BFS order or the binary tree above is `[1, 2, 3]`, so this tree will be serialized to `{1,2,3}`.\
Let's go through with an bigger binary tree:
```python
    1
   / \
  2   3
 / \   \
4   5   6
   / \
  7   8
```
it will be serialized to `{1,2,3,4,5,#,6,#,#,7,8}.`\
the left child and right child of 6, 7, 8 are all null, so they can be ignored as they are at the end of the bfs order.

### Code
```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:

    def serialize(self, root):
        """
        @param root: An object of TreeNode, denote the root of the binary tree.
        This method will be invoked first, you should design your own algorithm 
        to serialize a binary tree which denote by a root node to a string which
        can be easily deserialized by your own "deserialize" method later.
        """
        
        if not root:
            return "{}"
        queue = [root]
        count_idx = 0
        while count_idx < len(queue): # 一次做，所有層一起搞定，不需分層
            if queue[count_idx]:
                queue.append(queue[count_idx].left)
                queue.append(queue[count_idx].right)
            count_idx += 1
        while not queue[-1]: # 後面全不要
            queue.pop()
        return '{%s}' % ','.join([
            str(node.val) if node else '#'
            for node in queue
        ])

    def deserialize(self, data):
        """
        @param data: A string serialized by your serialize method.
        This method will be invoked second, the argument data is what exactly
        you serialized at method "serialize", that means the data is not given by
        system, it's given by your own serialize method. So the format of data is
        designed by yourself, and deserialize it here as you serialize it in 
        "serialize" method.

        root
        {1 | 2 3 | 4 5 # 6 |...}
             ^
         to_left_child is True; append to queue; to_left_child set to False
               ^
            to left_child is False; append to queue; index += 1 (new root); to_left_child set to True
        """

        data = data.strip('\n')
        if data == '{}':
            return None
        vals = data[1:-1].split(',')

        root = TreeNode(int(vals[0]))
        queue = [root] # 等待被加左右兒子
        count_idx = 0
        to_left_child = True
        for val in vals[1:]:
            if val is not '#':
                node = TreeNode(int(val))
                if to_left_child:
                    queue[count_idx].left = node
                else: # to right
                    queue[count_idx].right = node
                queue.append(node)
            count_idx += 1 if (to_left_child is False) else 0
            to_left_child = not to_left_child # switch
        return root
```
#### Remark:
- The `% operator` tells the Python interpreter to format a string using a given set of variables, enclosed in a tuple, following the operator. A very simple example of this is as follows:
`'%s is smaller than %s' % ('one', 'two')`
#### Submission:
```
761 ms
time cost
·
6.04 MB
memory cost
·
Your submission beats
45.20 %
Submissions
```
#### Complexity:
- Time: O(node)
- Space: O(node)
