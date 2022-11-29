## Heap (堆)
堆是一棵滿足如下性質的二叉樹：
- 父節點的鍵值總是不大於它的孩子節點的鍵值（小頂堆）。
- 父節點的鍵值總是不小於它的孩子節點的鍵值（大頂堆）。

由於堆是一棵形態規則的二叉樹，因此堆的父節點和孩子節點存在如下關係：
  > 可以把index 0拿來當作counter, 存這棵樹有幾個節點
  > 從index 1開始，節點的編號為`i`, 則其左孩子節點的編號為`2i`, 右孩子節點的編號為`2i+1`\
  > 子節點的編號為`i`, 則其父節點的編號為`i//2`(整數除法)
<p>
    <img src="https://iq.opengenus.org/content/images/2019/06/Min-Heap.png" width="500" />
</p>

由於上面的性質，父節點一定比他的兒節點小（大），所以整個樹的樹根的值一定是最小（最大）的，那麽我們就能**在O(1)的時間內，獲得整個堆的極值**。\
孩子之間不保證任何大小關係。

性質：
- O(logN) `add(element)`: 將進來的節點放在最下最左的新位子 -> 向上調整(sift up)
  -  樹有多高，就最多被上調幾次，所以保證操作為logN 
  <p>
    <img src="http://www.btechsmartclass.com/data_structures/ds_images/Max%20Heap%20Add%202.png" width="400" />
  </p>
  <p>
    <img src="http://www.btechsmartclass.com/data_structures/ds_images/Max%20Heap%20Add%203.png" width="400" />
  </p>

- O(logN) `poll()/pop()` （拿掉堆頂）
  - 用最末位的點換掉原堆頂，然後評估新堆頂，向下調整(sift down)
    - 注意：向下調整的時候不能與任意兒子換，如果是minHeap，一定要跟小的換，不然會破壞規則
    - 至多也是從最頂被調到最下，一樣是保證操作logN  
  <p>
    <img src="http://www.btechsmartclass.com/data_structures/ds_images/Max%20Heap%20Del%201.png" width="400" />
  </p>
  <p>
    <img src="http://www.btechsmartclass.com/data_structures/ds_images/Max%20Heap%20Del%202.png" width="400" />
  </p>
  <p>
    <img src="http://www.btechsmartclass.com/data_structures/ds_images/Max%20Heap%20Del%205.png" width="400" />
  </p>
  
- O(1) min or max `peek()` （看堆頂）
- O(N) `delete()/remove()` (刪除**任一**節點): 但必須保證該元素不重複 
  - 一樣是該元素跟最末節點交換，然後sift up 或 sift down (都有可能)
  - 如何快速找到該元素在樹的哪裡？**哈希表**(所以不能重複！)
    -   <key,value> = <元素, index>

結構：\
一定是從上到下、從左到右。所以知道節點數就一定知道樹的形狀。

例題：\
[Lint130](https://www.lintcode.com/problem/130/) - Heapify

## Heap and Priority Queue
優先隊列是一種抽象的數據類型，它和堆的關系類似於，List和數組、鏈表的關系一樣；我們常常使用堆來實現優先隊列，因此很多時候堆和優先隊列都很相似，它們只是概念上的區分。\
優先隊列的應用場景十分的廣泛，常見的應用有：
- Dijkstra’s algorithm（單源最短路問題中需要在鄰接表中找到某一點的最短鄰接邊，這可以將覆雜度降低。）
- Huffman coding（貪心算法的一個典型例子，采用優先隊列構建最優的前綴編碼樹(prefixEncodeTree)）
- Prim’s algorithm for minimum spanning tree

優先隊列是一個至少能夠提供插入（Insert）和刪除最小（DeleteMin）這兩種操作的數據結構。對應於隊列的操作，Insert相當於`Enqueue`，DeleteMin相當於`Dequeue`。\
用堆實現優先的過程中，需要注意最大堆只能對應最大優先隊列，最小堆則是對應最小優先隊列。
