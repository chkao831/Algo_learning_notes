## Heap (堆)
堆是一棵滿足如下性質的二叉樹：
- 父節點的鍵值總是不大於它的孩子節點的鍵值（小頂堆）。
- 父節點的鍵值總是不小於它的孩子節點的鍵值（大頂堆）。

由於堆是一棵形態規則的二叉樹，因此堆的父節點和孩子節點存在如下關系（根節點編號為0）：
  > 節點的編號為`i`, 則其左孩子節點的編號為`2i+1`, 右孩子節點的編號為`2i+2`\
  > 子節點的編號為`i`, 則其父節點的編號為`(i-1)//2`(整數除法)
<p>
    <img src="https://shubo.io/static/9a2c89211ed750fa9a30c3c06830ca76/bd9eb/array-representation.png" width="450" />
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
- O(N) `delete()/remove()` (刪除任一節點)

結構：\
一定是從上到下、從左到右。所以知道節點數就一定知道樹的形狀。
## Heap and Priority Queue
