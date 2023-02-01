### Longest Path With Different Adjacent Characters
https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
>Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.

<p>
    <img src="https://leetcode.com/problems/longest-path-with-different-adjacent-characters/solutions/2889382/Figures/2246/2246-1.png" width="800" />
</p>


```python
from collections import defaultdict
from typing import List, Set

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.root = 0

    def longestPath(self, parent: List[int], s: str) -> int:
        
        def create_graph(parent):
            for target, source in enumerate(parent):
                if source == -1:
                    self.root = target
                else:
                    self.graph[source].append(target)

        def dfs(node: int) -> int:
            nonlocal max_count, s
            
            max1, max2 = 0, 0
            for child in self.graph[node]:
                child_len = dfs(child)
                if s[child] == s[node]: # different adjacent
                    continue
                if child_len > max1: # child > max1 > max2
                    max2 = max1
                    max1 = child_len
                elif child_len > max2:
                    max2 = child_len
                
            max_count = max(max_count, 1+max1+max2)
            return 1+max1

        create_graph(parent)
        max_count = 1
        dfs(node=self.root)

        return max_count
```
#### Remark:
- Key: bottom up DFS, 從葉子更新first max, second max (two chain分別的長度)，然後return目前為止最長的那一條
#### Submission:
```
Runtime
1794 ms
Beats
55.18%

Memory
150.1 MB
Beats
69.50%
```
#### Complexity:
- Time: O(n)
- Space: O(n)
