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
- Space: O(roads) for graph construction

## b. 暴力DFS + 最優性剪枝 (prunning, or Optimal Prunning Algorithm)
- 多一個參數`path`傳進去`dfs()`紀錄
- 使用`prunning()`這個function進行反轉

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
            graph = {}
            for road in roads:
                city_1, city_2, cost = road[0], road[1], road[2]

                if city_1 in graph.keys():
                    existing_cost = graph.get(city_1,{}).get(city_2)
                    graph[city_1][city_2] = min(cost, existing_cost) if existing_cost else cost
                else:
                    graph[city_1] = {city_2: cost}

                if city_2 in graph.keys():
                    existing_cost = graph.get(city_2,{}).get(city_1)
                    graph[city_2][city_1] = min(cost, existing_cost) if existing_cost else cost
                else:
                    graph[city_2] = {city_1: cost}

            return graph

        def dfs(startingCity: int, set_visited: Set, curr_cost: int, path: List):
            # base
            if len(set_visited) == n:
                self.global_mincost = min(self.global_mincost, curr_cost)
                return
            # recursive
            for nextCity in graph[startingCity]:
                if nextCity in set_visited:
                    continue
                if prunning(nextCity, path):
                    continue
                set_visited.add(nextCity)
                path.append(nextCity)
                dfs(nextCity, set_visited, curr_cost+graph[startingCity][nextCity], path)
                set_visited.remove(nextCity)
                path.pop()

        def prunning(nextCity: int, path: List) -> bool:
            """
            index =     i-1 i   -1  
            pre  = 1  2  3  4 5  6  nextCity  [3(i-1) <-> 4(i); 6(-1) <-> nextCity]
            post = 1  2  3  6 5  4  nextCity  [3(i-1) <-> 6(-1); 4(i) <-> nextCity]
            """
            for i in range(1, len(path)):
                post_1 = float('inf') if not graph.get(path[i-1]).get(path[-1]) else graph[path[i-1]][path[-1]]
                post_2 = float('inf') if not graph.get(path[i]).get(nextCity) else graph[path[i]][nextCity]
                if graph[path[i-1]][path[i]] + graph[path[-1]][nextCity] > post_1 + post_2:
                    return True # when pre-prunning path is longer
            return False

        graph = construct_graph()
        dfs(startingCity=1, set_visited=set([1]), curr_cost=0, path=[1])
        return self.global_mincost
```
#### Remark:
- 在`construct_graph()`裡面，要把`defaultdict`換回普通`dict`了
    - 因為在`prunning()`裡，我們要去比一些**可能不存在字典**裡的路徑，本來想著把defaultdict初始成`defaultdict(lambda: defaultdict(lambda: float('inf')))`這樣的形式(表示他是一個`nested defaultdict, with inner value set to float('inf')`)，這樣當找不到路的時候，可以返回無限大的值，代表此路不通。
    - 但是，defaultdict在`prunning()`裡面遇到這樣的情況會自動生出路，這樣回到`dfs()`裡面就會報錯: `RuntimeError: dictionary changed size during iteration`
    - 只好用回普通dictionary, 用比較傳統的方式去safeget, **get不到會返回None**, 此時再在`prunning()`裡面設成inf即可，不會自動生成值。
- 最優性剪枝
    - 為什麼只處理倒數第一項到前面的反轉，不處理中間跟中間的？
        - 倒數第二，舉例來說，在倒數第一這個點被加進來的時候就已經被試過了
        - 因此，我們只處理新增這個點，影響到`nextCity`的連結的反轉
    - 為什麼不把`nextCity`一起算進來轉？
        - 我們不知道`nextCity`之後連什麼，如果一起轉，可能就連不到了。必須保證前後關係。    
#### Submission:
```
122 ms
time cost
·
6.06 MB
memory cost
·
Your submission beats
82.60 %
Submissions
```
#### Complexity:
- Time: O(n * n!)
- Space: O(roads) for graph construction
