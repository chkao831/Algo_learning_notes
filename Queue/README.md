## Queue (隊列)
- FIFO
- Common Application: BFS
- Storage Type
  - Linked List (鏈表)：對插入和刪除有較好性能 
  - array (數組)：對隨機訪問有較好性能
- Function
  - `__init__`: 初始化隊列
  - `enqueue(item)`: 向隊尾插入元素
  - `dequeue()`: 刪除並返回隊首元素
### Linked List
- 由多個Node所組成, 一個Node由兩個部分 - 數據域 + 指針域 所組成
- [Singly Linked List Implementation](https://github.com/chkao831/Algo_learning_notes/blob/main/Queue/LintCode_492_Implement-Queue-by-Linked-List.md)
- [Doubly Linked List Implementation](https://github.com/chkao831/Algo_learning_notes/blob/main/Queue/LintCode_493_Implement-Queue-by-Linked-List-II.md) (with addition of `push_front(item)` and `pop_back()` functions)

### Array
####
