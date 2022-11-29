```
堆是一棵滿足如下性質的二叉樹：
1、父節點的鍵值總是不大於它的孩子節點的鍵值（小頂堆）。
2、父節點的鍵值總是不小於它的孩子節點的鍵值（大頂堆）。
由於堆是一棵形態規則的二叉樹，因此堆的父節點和孩子節點存在如下關系（根節點編號為0）：
設父節點的編號為 i, 則其左孩子節點的編號為2i+1, 右孩子節點的編號為2i+2
設孩子節點的編號為i, 則其父節點的編號為(i-1)/2
由於上面的性質，父節點一定比他的兒節點小（大），所以整個樹的樹根的值一定是最小（最大）的，那麽我們就能在O(1)的時間內，獲得整個堆的極值。
現在有沒有發現堆和我們曾經遇到過的優先隊列具有很相似的特點，那麽二者究竟有何聯系呢？

優先隊列是一種抽象的數據類型，它和堆的關系類似於，List和數組、鏈表的關系一樣；我們常常使用堆來實現優先隊列，因此很多時候堆和優先隊列都很相似，它們只是概念上的區分。
優先隊列的應用場景十分的廣泛，常見的應用有：
Dijkstra’s algorithm（單源最短路問題中需要在鄰接表中找到某一點的最短鄰接邊，這可以將覆雜度降低。）
Huffman coding（貪心算法的一個典型例子，采用優先隊列構建最優的前綴編碼樹(prefixEncodeTree)）
Prim’s algorithm for minimum spanning tree
在java，python中都已經有封裝了的Priority Queue(Heaps)
優先隊列是一個至少能夠提供插入（Insert）和刪除最小（DeleteMin）這兩種操作的數據結構。對應於隊列的操作，Insert相當於Enqueue，DeleteMin相當於Dequeue。
用堆實現優先的過程中，需要注意最大堆只能對應最大優先隊列，最小堆則是對應最小優先隊列。

現在我們借助下面的問題，來理解shiftup和shiftdown的思想。
給定一個數組A[]，我們的目的是要將 A[] 堆化，也就是讓A[]滿足以下要求：
A[i * 2 + 1] >= A[i]
A[i * 2 + 2] >= A[i]

基於 shiftup的版本 O(nlogn)
Java版本：
public class Solution {
    /**
     * @param A: Given an integer array
     * @return: void
     */
    private void siftup(int[] A, int k) {
        while (k != 0) {
            int father = (k - 1) / 2;
            if (A[k] > A[father]) {
                break;
            }
            int temp = A[k];
            A[k] = A[father];
            A[father] = temp;
            
            k = father;
        }
    }
    
    public void heapify(int[] A) {
        for (int i = 0; i < A.length; i++) {
            siftup(A, i);
        }
    }
}
Python版本：
class Solution:
    # @param A: Given an integer array
    # @return: void
    def siftup(self, A, k):
        while k != 0:
            father = (k - 1) // 2
            if A[k] > A[father]:
                break
            A[k], A[father] = A[father], A[k]
            k = father
            
    def heapify(self, A):
        for i in range(len(A)):
            self.siftup(A, i)
           
算法思路：
對於每個元素A[i]，比較A[i]和它的父親結點的大小，如果小於父親結點，則與父親結點交換。
交換後再和新的父親比較，重覆上述操作，直至該點的值大於父親。
時間覆雜度分析：
對於每個元素都要遍歷一遍，這部分是 O(n)
每處理一個元素時，最多需要向根部方向交換 logn次。
因此總的時間覆雜度是 O(nlogn)

除了上面的代碼，我們也可以使用更有效率的O(n)的算法。
基於 Siftdown 的版本 O(n)
Java版本：
public class Solution {
    /**
     * @param A: Given an integer array
     * @return: void
     */
    private void siftdown(int[] A, int k) {
        while (k * 2 + 1 < A.length) {
            int son = k * 2 + 1;   // A[i] 的左兒子下標。
            if (k * 2 + 2 < A.length && A[son] > A[k * 2 + 2])
                son = k * 2 + 2;     // 選擇兩個兒子中較小的。
            if (A[son] >= A[k])      
                break;
            
            int temp = A[son];
            A[son] = A[k];
            A[k] = temp;
            k = son;
        }
    }
    
    public void heapify(int[] A) {
        for (int i = (A.length - 1) / 2; i >= 0; i--) {
            siftdown(A, i);
        }
    }
}
Python版本：
import sys
import collections
class Solution:
    # @param A: Given an integer array
    # @return: void
    def siftdown(self, A, k):
        while k * 2 + 1 < len(A):
            son = k * 2 + 1    #A[i]左兒子的下標
            if k * 2 + 2 < len(A) and A[son] > A[k * 2 + 2]:
                son = k * 2 + 2    #選擇兩個兒子中較小的一個
            if A[son] >= A[k]:
                break
                
            temp = A[son]
            A[son] = A[k]
            A[k] = temp
            k = son
    
    def heapify(self, A):
        for i in range((len(A) - 1) // 2, -1, -1):
            self.siftdown(A, i)
         
算法思路：
初始選擇最接近葉子的一個父結點，與其兩個兒子中較小的一個比較，若大於兒子，則與兒子交換。
交換後再與新的兒子比較並交換，直至沒有兒子。
再選擇較淺深度的父親結點，重覆上述步驟。
時間覆雜度分析
這個版本的算法，乍一看也是 O(nlogn)， 但是我們仔細分析一下，算法從第 n/2 個數開始，倒過來進行 siftdown。也就是說，相當於從 heap 的倒數第二層開始進行 siftdown 操作，倒數第二層的節點大約有 n/4 個， 這 n/4 個數，最多 siftdown 1次就到底了，所以這一層的時間覆雜度耗費是 O(n/4)，然後倒數第三層差不多 n/8 個點，最多 siftdown 2次就到底了。所以這里的耗費是 O(n/8 * 2), 倒數第4層是 O(n/16 * 3)，倒數第5層是 O(n/32 * 4) ... 因此累加所有的時間覆雜度耗費為：
T(n) = O(n/4) + O(n/8 * 2) + O(n/16 * 3) ...
然後我們用 2T - T 得到：
2 * T(n) = O(n/2) + O(n/4 * 2) + O(n/8 * 3) + O(n/16 * 4) ...
T(n) = O(n/4) + O(n/8 * 2) + O(n/16 * 3) ...
2 * T(n) - T(n) = O(n/2) +O (n/4) + O(n/8) + ...
= O(n/2 + n/4 + n/8 + ... )
= O(n)
因此得到 T(n) = 2 * T(n) - T(n) = O(n)

堆排序

運用堆的性質，我們可以得到一種常用的、穩定的、高效的排序算法————堆排序。堆排序的時間覆雜度為O(n*log(n))，空間覆雜度為O(1)，堆排序的思想是：對於含有n個元素的無序數組nums, 構建一個堆(這里是小頂堆)heap，然後執行extractMin得到最小的元素，這樣執行n次得到序列就是排序好的序列。
如果是降序排列則是小頂堆；否則利用大頂堆。
Trick

由於extractMin執行完畢後，最後一個元素last已經被移動到了root，因此可以將extractMin返回的元素放置於最後，這樣可以得到sort in place的堆排序算法。
當然，如果不使用前面定義的heap，則可以手動寫堆排序，由於堆排序設計到建堆和extractMin， 兩個操作都公共依賴於siftDown函數，因此我們只需要實現siftDown即可。(trick:由於建堆操作可以采用siftUp或者siftDown，而extractMin是需要siftDown操作，因此取公共部分，則采用siftDown建堆)。
升序堆排序（JAVA）

public class Solution {
    private void siftdown(int[] A, int left, int right) {
        int k = left;
        while (k * 2 + 1 <= right) {
            int son = k * 2 + 1;
            if (son + 1 <= right && A[son] < A[son + 1]) {
                son = k * 2 + 2;
            }
            if (A[son] <= A[k]) {
                break;
            }
            int tmp = A[son];
            A[son] = A[k];
            A[k] = tmp;
            k = son;
        }
    }
    
    public void heapify(int[] A) {
        for (int i = (A.length - 1) / 2; i >= 0; i--) {
            siftdown(A, i, A.length - 1);
        }
    }
    
    void sortIntegers(int[] A) {
        heapify(A);
        for (int i = A.length - 1; i > 0; i--) {
            int tmp = A[0];
            A[0] = A[i];
            A[i] = tmp;
            siftdown(A, 0, i - 1);
        }
    }
}
```
