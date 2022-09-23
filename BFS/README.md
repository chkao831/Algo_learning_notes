## Breadth First Search (BFS)
### 使用須知
能夠用BFS解決的問題，一定不要用DFS去做！（DFS有StackOverflow風險）

### 適用場景
- 分層遍歷
  - 一層層遍歷一個圖、樹、矩陣
    - 圖：大家都是平等的，存在環，需要哈希表，因為同一個節點可能重複進入隊列
      - BFS中，同一個節點不需要重複進行隊列，因為連通塊不可能帶來新的節點、最短路不可能帶來更短的路徑
      - Python去重：`dict`(需要存儲分層信息/次數信息) | `set`(只需要紀錄是否出現過)
    - 樹：是圖的一種，從上往下的父子關係，不會出現環（是沒有環的圖）
  - 簡單圖（圖中所有邊長都一樣）**最短路徑**
    - 第一次BFS走到某個點，那條路一定是最短路徑 
    - 遇到複雜圖時，有Floyd, Kijkstra, Bellman-ford, SPFA, 但複雜圖的最短路徑面試不常見
    - 最長路徑：BFS不行
      - 若圖可以分層(路徑有一定方向性，不能繞圈)，使用DP
      - 若圖不可以進行分層，使用DFS
- 連通塊問題
  - 通過圖中一個點找到其他所有連通的點
  - 找到所有方案問題的一種非遞歸實現方式 
- 拓撲排序：實現容易度>DFS 
  - 求任意拓排序
  - 求是否有拓排序
  - 求字典序最小的拓排序
  - 求是否唯一拓排序
### 實現方法：Python建議使用`deque`, 因為`Queue`涉及到多線程加鎖，慢。
https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LeetCode_102_Binary-Tree-Level-Order-Traversal.md
- 單隊列
- 雙隊列
- DummyNode
### 通用模板
distance dict的key用於判斷是否已經訪問過; value用於記錄最短節點距離
```python
queue = collections.deque([node])
distance = {node: 0} # 如果只記錄是/否訪問過, set即可; dict是拿來存儲分層信息的

while queue: # 每次pop一個節點出來
    node = queue.popleft() # O(N)
    for neighbor in node.get_neighbors(): # 並拓展相鄰節點, O(2*M)
        if neighbor in distance:
            continue
        queue.append(neighbor) # 和下一行hashmap加元素貼緊
        distance[neighbor] = distance[node] + 1 # 和上一行入隊貼緊
```
N個點、M條邊，圖上BFS時間複雜度=O(N+2*M)=O(N+M)，一般可以說是O(M)，因為邊一般都比點多\
M最大為O(N^2)的級別（任兩點之間都有邊），所以worst case是O(N^2)

如果真的想要每次while是處理一層，不是一個節點的話，也可以，就是多一個for loop。但還是建議上述模板。
```python
queue = collections.deque([node])
distance = {node: 0}

while queue: # 每次pop一層出來
    for _ in range(len(queue)):
        node = queue.popleft()
        for neighbor in node.get_neighbors():
            if neighbor in distance:
                continue
            queue.append(neighbor)
            distance[neighbor] = distance[node] + 1
```
### 拓撲排序
- In-degree (入度):
  -  指 **有向圖(Directed Graph)** 中指向當前節點的點(或邊)的個數
- Algorithm
  - (1) 統計每個點的In-degree
  - (2) 將每個In-degree=0放入Queue中作為起始節點 （In-degree=0代表不依附於任何點）
  - (3) 不斷從Queue中拿出一個點，去掉這個點的所有連邊，其他點的相應In-degree=-1
  - (4) 一但發現新的In-degree=0的點，丟回Queue中
- 一個圖可能存在多個Topological Order, 也可能不存在任何Topological Order

