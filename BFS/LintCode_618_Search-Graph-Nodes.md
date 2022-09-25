### Search Graph Nodes
https://www.lintcode.com/problem/618/
> 給定一張 無向圖，一個 節點 以及一個 目標值，返回距離這個節點最近 且 值為目標值的節點，如果不能找到則返回 NULL。\
> 在給出的參數中, 我們用 map 來存節點的值
```python
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph: list, values: dict, node: "UndirectedGraphNode", target: int):
        if not graph: 
            return None
        queue = collections.deque([node])
        set_visited = set([node])
        while queue:
            node = queue.popleft()
            if values[node] == target:
                return node
            for neighbor in node.neighbors:
                if neighbor in set_visited:
                    continue
                queue.append(neighbor)
                set_visited.add(neighbor)
        return None

```
#### Remark:
- Forgot the `[]` brackets in `queue = collections.deque([node])` and `set_visited = set([node])`
#### Submission:
```
1046 ms
time cost
·
6.59 MB
memory cost
·
Your submission beats
29.80 %
Submissions
```
#### Complexity:
- Time: O(max(node, edge))
- Space: O(node)
