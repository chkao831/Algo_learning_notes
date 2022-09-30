### Topological Sorting
https://www.lintcode.com/problem/127/
>Given an directed graph, a topological order of the graph nodes is defined as follow:
>
>For each directed edge `A -> B` in graph, A must before B in the order list.\
>The first node in the order can be any node in the graph with no nodes direct to it.\
>Find any topological order for the given graph.\
>You can assume that there is at least one topological order in the graph.
>
```python
"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:

    def __init__(self):
        self.node_inDegree = {}

    def topSort(self, graph):
        """
        @param graph: A list of Directed graph node
        @return: Any topological order for the given graph.
        """

        def get_dict_nodeInDegree():
            self.node_inDegree = {n: 0 for n in graph}
            for node in graph:
                for neighbor in node.neighbors:
                    self.node_inDegree[neighbor] = self.node_inDegree.get(neighbor, 0) + 1

        get_dict_nodeInDegree()
        order = []
        starting_nodes = [n for n in graph if self.node_inDegree[n]==0]
        queue = collections.deque(starting_nodes)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                self.node_inDegree[neighbor] -= 1
                if self.node_inDegree[neighbor] == 0:
                    queue.append(neighbor)
        return order
```
#### Remark:
- 
#### Submission:
```
142 ms
time cost
·
10.66 MB
memory cost
·
Your submission beats
98.40 %
Submissions
```
#### Complexity:
- 假設n個點，m條邊；
     - 記錄拓撲序空間複雜度為O(n)，記錄入度最壞複雜度為O(n)，空間複雜度O(n)；
     - 記錄每個點的入度為O(m)，拓撲排序為O(m)，時間複雜度O(m)。

