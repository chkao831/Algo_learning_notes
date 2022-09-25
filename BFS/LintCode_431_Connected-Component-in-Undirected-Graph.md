### Connected Component in Undirected Graph
https://www.lintcode.com/problem/431/description
>找出無向圖中所有的連通塊。
>
>圖中的每個節點包含一個label屬性和一個鄰接點的列表。
>
>（一個無向圖的連通塊是一個子圖，其中任意兩個頂點通過路徑相連，且不與整個圖中的其它頂點相連。）
>
>你需要返回 label 集合的列表.

> **Nodes in a connected component should sort by label in ascending order. Different connected components can be in any order.**
```python
from typing import (
    List,
)
from lintcode import (
    UndirectedGraphNode,
)

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    
    def __init__(self):
        self.set_visited = set()

    def connectedSet(self, nodes: List[UndirectedGraphNode]) -> List[List[int]]:
        """
        @param nodes: a array of Undirected graph node
        @return: a connected set of a Undirected graph
        """

        def bfs(node: UndirectedGraphNode) -> List:
            queue = collections.deque([node])
            self.set_visited.add(node)
            set_subgraph = set([node.label])
            while queue:
                node = queue.popleft()
                for neigh in node.neighbors:
                    if neigh in self.set_visited:
                        continue
                    queue.append(neigh)
                    self.set_visited.add(neigh)
                    set_subgraph.add(neigh.label)
            return sorted(list(set_subgraph))

        list_subgraph = []
        if not nodes:
            return list_subgraph
        for node in nodes:
            if node not in self.set_visited:
                list_subgraph.append(bfs(node))
        return list_subgraph
```
#### Remark:
- Forgot to sort subgraph lists by label in ascending order
  - need to append `neigh.label` to the returning list/set, not `neigh`(node) itself. 
#### Submission:
```
247 ms
time cost
·
13.25 MB
memory cost
·
Your submission beats
26.20 %
Submissions

```
#### Complexity:
- Time: O(max(vertices, edges))
- Space: O(vertices)
