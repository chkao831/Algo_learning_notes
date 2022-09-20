# Queue (隊列)

## 普通隊列
- FIFO
- Common Application: BFS
- Storage Type
  - Linked List (鏈表)：對插入和刪除有較好性能 
  - array (數組)：對隨機訪問有較好性能，因為Linked List要移動指針
- Function
  - `__init__`: 初始化隊列
  - `enqueue(item)`: 向隊尾插入元素
  - `dequeue()`: 刪除並返回隊首元素
### Array
需要創建一個固定長度的數組作為隊列，還需要附設兩個變量head & tail分別指示首尾的位置。\
每次元素入隊時，tail向後移動。出隊時，head向後移動。\
**然而**，使用一般二維數組實現隊列的話，會出現空間不能有效被利用的情況（以為已經滿了(tail到底了)但是實際上還可以繼續添加元素，稱為`假溢出`）\
所以要使用Circular Array或Linked List來實現
#### Circular Array
將向量空間想像為一個首尾相接的圓環，存儲在其中的隊列稱為循環隊列，其將順序隊列首尾相連。
- [Circular Array Implementation](https://github.com/chkao831/Algo_learning_notes/blob/main/Queue/LintCode_955_Implement-Queue-by-Circular-Array.md)

### Linked List
- 由多個Node所組成, 一個Node由兩個部分 - 數據域 + 指針域 所組成
- [Singly Linked List Implementation](https://github.com/chkao831/Algo_learning_notes/blob/main/Queue/LintCode_492_Implement-Queue-by-Linked-List.md)
- [Doubly Linked List Implementation](https://github.com/chkao831/Algo_learning_notes/blob/main/Queue/LintCode_493_Implement-Queue-by-Linked-List-II.md) (with addition of `push_front(item)` and `pop_back()` functions)


## Priority Queue
- 基於堆(Heap)實現
- 非FIFO(最先出隊列的是優先級最高的元素)
