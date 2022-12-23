### Sum of Distances in Tree
https://leetcode.com/problems/sum-of-distances-in-tree/description/
>There is an **undirected connected tree** with `n` nodes labeled from `0` to `n - 1` and `n - 1` edges.
>
>You are given the integer `n` and the array edges where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the tree.
>
>Return an array answer of length `n` where `answer[i]` is the sum of the distances between the ith node in the tree and all other nodes.

For neighboring nodes `x` and `y`, 
<p>
    <img src="https://leetcode.com/problems/sum-of-distances-in-tree/solutions/130611/Figures/834/sketch1.png" width="700" />
</p>

=> `ans[x] - ans[y] = #(Y) - #(X)`

Let `count[node]` be the number of nodes in the subtree of `node`, and `stsum[node]` ("subtree sum") be the sum of the distances from node to the nodes in the subtree. 
1. **Bottom up DFS** to give us the right answer for the root: `ans[root] = stsum[root]` (postorder trav.)
2. **Top down DFS** for leaves (preorder trav.)
 
<p>
    <img src="https://leetcode.com/problems/sum-of-distances-in-tree/solutions/130611/Figures/834/sketch2.png" width="700" />
</p>

By `ans[child] - ans[parent] = (N - count[child]) - count[child]`, \
`ans[child] = ans[parent] - count[child] + (N - count[child])` 

```python
class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * N
        ans = [0] * N
        def dfs(node: int, parent: int = None): # bottom up
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node: int, parent: int = None): # top down
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + N - count[child]
                    dfs2(child, node)

        dfs(node=0)
        dfs2(node=0)
        return ans
```
#### Remark:
- Distinguish between bottom up and top down DFS
#### Submission:
```
Runtime
2685 ms
Beats
25.27%

Memory
66 MB
Beats
25.81%
```
#### Complexity:
- Time: O(N)
- Space: O(N)
