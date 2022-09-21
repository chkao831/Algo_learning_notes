## Breadth First Search (BFS)
### 適用場景
- 分層遍歷
  - 一層層遍歷一個圖、樹、矩陣
  - 簡單圖（圖中所有邊長都一樣）最短路徑
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
### 實現方法
https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LeetCode_102_Binary-Tree-Level-Order-Traversal.md
- 單隊列
- 雙隊列
- DummyNode
