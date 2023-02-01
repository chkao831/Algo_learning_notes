### Number of Nodes in the Sub-Tree With the Same Label
https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
>Return an array of size `n` where `ans[i]` is the number of nodes in the subtree of the ith node which have the same label as node `i`.

<p>
    <img src="https://assets.leetcode.com/uploads/2020/07/01/q3e1.jpg" width="500" />
</p>

```python
from collections import defaultdict, Counter

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        def create_graph(edges):
            for n1, n2 in edges:
                self.graph[n1].append(n2)
                self.graph[n2].append(n1)
        
        def dfs(node: int, visited: List[bool]) -> Counter:
            nonlocal labels, out
            visited[node] = True

            # recursive
            counter = Counter()
            for neigh in self.graph[node]:
                if not visited[neigh]:
                    # Update count with the letters' frequency in the children nodes
                    counter += dfs(neigh, visited)

            counter[labels[node]] += 1
            out[node] = counter[labels[node]]
            return counter

        create_graph(edges)
        out = [0]*n
        dfs(node=0, visited=[False for _ in range(n)])
        return out
```
#### Remark:
- 回傳Counter, bottom up, 依照葉子回傳的counter疊加上去
#### Submission:
```
Runtime
3122 ms
Beats
28.18%

Memory
169.6 MB
Beats
82.15%
```
#### Complexity:
- Time: O(n)
- Space: O(n)
