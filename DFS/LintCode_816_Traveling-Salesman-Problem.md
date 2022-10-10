# Traveling Salesman Problem (TSP)
https://www.lintcode.com/problem/816/
>Give `n` cities (labeled from `1` to `n`), and the undirected road's `cost` among the cities as a three-tuple `[A, B, c]`\
>(i.e there is a road between city `A` and city `B` and the `cost` is `c`). \
>We need to **find the smallest cost to travel all the cities starting from 1**.

<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/Euler12.png" />

- 排列式搜索的典型代表
- 著名的NP問題(non-deterministic polynomial-time)
- DP解法是加分項

## a. 暴力DFS

```python
from typing import (
    List, Mapping, Set
)
from collections import defaultdict

class Solution:
    
    def __init__(self):
        # if choose not to pass into dfs() and need to revise its value dynamically, 
        # must declare it as global variable
        self.global_mincost = float('inf')

    def min_cost(self, n: int, roads: List[List[int]]) -> int:
        """
        @param n: an integer,denote the number of cities
        @param roads: a list of three-tuples,denote the road between cities
        @return: return the minimum cost to travel all cities
        """

        def construct_graph() -> Mapping[int, Mapping[int, int]]:
            """
            graph = { sourceCity (int) : { destinationCity (int): cost (int) } ...}
            """
            graph = defaultdict(lambda: defaultdict(dict))
            for road in roads:
                city_1, city_2, cost = road[0], road[1], road[2]
                graph[city_1][city_2] = min(cost, graph[city_1][city_2]) if graph[city_1][city_2] else cost
                graph[city_2][city_1] = min(cost, graph[city_2][city_1]) if graph[city_2][city_1] else cost
            return graph

        def dfs(startingCity: int, set_visited: Set, curr_cost: int):
            # base
            if len(set_visited) == n:
                self.global_mincost = min(self.global_mincost, curr_cost)
                return
            # recursive
            for nextCity in graph[startingCity]:
                if nextCity in set_visited:
                    continue
                set_visited.add(nextCity)
                dfs(nextCity, set_visited, curr_cost+graph[startingCity][nextCity])
                set_visited.remove(nextCity)

        graph = construct_graph()
        dfs(startingCity=1, set_visited=set([1]), curr_cost=0)
        return self.global_mincost
```
#### Remark:
- graph構建: `dict` of `dict`, initialize roads as `float('inf')`
  - city `index starts from 1`, so it's in `range(1, n+1)`
  - Type hint for nested Dict: `Mapping[int, Mapping[int, int]]`, instead of `Dict[Dict[int]]`
- record visited cities in a `set()`; remember to initialize the set with `city 1` in it.  
- To initialize **defaultdict of defaultdict**: `defaultdict(lambda: defaultdict(dict))`
- **注意：不可以在每一次的recursive `dfs()` call前，先`curr_cost += graph[startingCity][nextCity]`, 否則在後面也會需要backtrack減回來**
#### Submission:
```
823 ms
time cost
·
5.99 MB
memory cost
·
Your submission beats
11.60 %
Submissions
```
#### Complexity:
- Time: O(n * n!)
- Space: O(n) for graph construction

## b. 暴力DFS + 最優性剪枝 (prunning, or Optimal Prunning Algorithm)

```python
```
#### Remark:
- 
#### Submission:
```
```
#### Complexity:
- Time:
- Space:
