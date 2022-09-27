### 
<link>
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
- Time:
- Space:
