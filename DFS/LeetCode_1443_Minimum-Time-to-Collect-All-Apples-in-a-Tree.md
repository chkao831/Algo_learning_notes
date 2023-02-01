### Minimum Time to Collect All Apples in a Tree
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/
>Given an **undirected** tree consisting of n vertices numbered from `0` to `n-1`, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex `0` and coming back to this vertex.

<p>
    <img src="https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/solutions/2864715/Figures/1443/1443-3.png" width="800" />
</p>

```python
from collections import defaultdict

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.count = 0

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        def create_graph(edges):
            for edge in edges:
                self.graph[edge[0]].append(edge[1])
                self.graph[edge[1]].append(edge[0])
        
        def dfs(node: int, hasApple: List[bool], visited: List[bool]):
            apple = False
            if hasApple[node]:
                apple = True

            # bottom up dfs
            visited[node] = True
            for neigh in self.graph[node]:
                if not visited[neigh]: # directed, down
                    if dfs(neigh, hasApple, visited):
                        self.count += 2
                        apple = True # when at least one child has apple, this path must be taken

            return apple

        create_graph(edges)
        dfs(node=0, hasApple=hasApple, visited=[False for _ in range(n)])
        return self.count
```
#### Submission:
```
Runtime
718 ms
Beats
80.77%

Memory
50.8 MB
Beats
74.36%
```
#### Complexity:
- Time: O(N)
- Space: O(N)
