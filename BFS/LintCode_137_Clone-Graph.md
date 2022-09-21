### Clone Graph
https://www.lintcode.com/problem/137/

連通塊問題\
G = <V, E>

<p>
    <img src="../images/137_Clone-Graph.jpg" width="500" />
</p>

此題解題步驟分三步：
- 找到所有點
- 複製所有點(用一個dictionary建立新舊節點映射關係 `{'old_node': 'new_node'}`)
- 複製所有邊

>Clone an undirected graph. Each node in the graph contains a `label` and a list of its `neighbors`. Nodes are labeled uniquely.
>
>You need to return a deep copied graph, which has the same structure as the original graph, and any changes to the new graph will not have any effect on the original graph.

```python
from lintcode import (
    UndirectedGraphNode,
)

"""
Definition for a UndirectedGraphNode:
class UndirectedGraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = []
"""

class Solution:
    
    def __init__(self):
        self.dict_cloned = {}
        self.list_visited_nodes = []

    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        """
        @param node: A undirected graph node
        @return: A undirected graph node
        """

        def find_vertices():

            queue = collections.deque([node])
            set_visited_nodes = set([node])
            while queue:
                n = queue.popleft()
                for neighbor in n.neighbors:
                    if neighbor in set_visited_nodes:
                        continue
                    queue.append(neighbor)
                    set_visited_nodes.add(neighbor)
            self.list_visited_nodes = list(set_visited_nodes)
        
        def clone_vertices():
            for node in self.list_visited_nodes:
                self.dict_cloned[node] = UndirectedGraphNode(node.label)
        
        def clone_edges():
            for node in self.list_visited_nodes:
                new_node = self.dict_cloned[node]
                for old_neighbor in node.neighbors:
                    new_neighbor = self.dict_cloned[old_neighbor]
                    new_node.neighbors.append(new_neighbor)

        if not node:
            return None
        find_vertices()
        clone_vertices()
        clone_edges()
        return self.dict_cloned[node]
```
#### Remark:
- Mistakes:
    - 在`clone_edges()`裡，忘記用inner for loop映射old neighbor and new neighbor
    - 在`find_vertices()`裡，重複把兩個不同的東西都取名為`node`，一個是外面那層的starting node，一個是while loop裡面pop出來的，外面那層進來若是沒有用傳的，不能重名。
#### Submission:
```
122 ms
time cost
·
8.32 MB
memory cost
·
Your submission beats
47.20 %
Submissions
```
#### Complexity:
- Time: O(n+m), where n is the number of nodes (vertices) and m is the number of edges.
- Space: O(n)
