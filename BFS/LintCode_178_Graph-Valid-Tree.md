### Graph Valid Tree
https://www.lintcode.com/problem/178/description
>Given `n` nodes labeled from `0` to `n - 1` and a list of `undirected` edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
```python
from typing import (
    List,
)

class Solution:
    
    def __init__(self):
        self.dict_node_neighbor = {}
        self.set_visited_node = set()

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        """
        @param n: An integer
        @param edges: a list of undirected edges
        @return: true if it's a valid tree, or false
        """

        def create_dict_node_neighbor(): # dict = {node: [neigh1, neigh2, ...]}
            for edge in edges:
                self.dict_node_neighbor[edge[0]] = self.dict_node_neighbor.get(edge[0], []) + [edge[1]]
                self.dict_node_neighbor[edge[1]] = self.dict_node_neighbor.get(edge[1], []) + [edge[0]]

        if n < 1: return False
        if len(edges) != (n-1): return False
        create_dict_node_neighbor()
        
        queue = collections.deque([0]) # nodes are labelled from 0
        self.set_visited_node.add(0)
        while queue:
            node = queue.popleft()
            for neighbor in self.dict_node_neighbor.get(node, []):
                if neighbor in self.set_visited_node:
                    continue
                queue.append(neighbor)
                self.set_visited_node.add(neighbor)
        return len(self.set_visited_node)==n
```
#### Remark:
- 一棵擁有n個節點的樹有n-1條邊，樹是連通的，沒有環的。
  - 給定一個無向圖讓我們判斷是否為樹，我們只需要判斷是否連通且無環即可。
- 我們可以從根節點出發向兒子節點進行廣度優先搜索bfs，如果能遍歷完所有的點，且沒有環存在，那麼說明這個無向圖是樹。
- Mistake1: Originally wrote this...this doesn't work. This is because `append` is an in-place operation.
  ```python
  for edge in edges:
    self.dict_node_neighbor[edge[0]] = self.dict_node_neighbor.get(edge[0], []).append(edge[1])
    self.dict_node_neighbor[edge[1]] = self.dict_node_neighbor.get(edge[1], []).append(edge[0])
  ```
  Alternatively, use `defaultdict` (see Lint605)
  ```python
  self.dict_node_neighbor = defaultdict(list)
  for edge in edges:
    self.dict_node_neighbor[edge[0]].append(edge[1])
    self.dict_node_neighbor[edge[1]].append(edge[0])
  ```
- Mistake2: forgot to assign default (forgot safe dictionary retrieval)
  ```python
  for neighbor in self.dict_node_neighbor[node]:
  ```
#### Submission:
```
103 ms
time cost
·
6.78 MB
memory cost
·
Your submission beats
57.60 %
Submissions
```
#### Complexity:
- Time: O(V+E) = O(max(V, E))
- Space: O(V)
