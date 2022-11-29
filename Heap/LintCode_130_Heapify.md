## Heapify
https://www.lintcode.com/problem/130/
>Given an integer array, heapify it into a min-heap array.

本題中，堆的父節點和孩子節點存在如下關系（根節點編號為0）：
- 設父節點的編號為`i`, 則其左孩子節點的編號為`2i+1`, 右孩子節點的編號為`2i+2`
- 設孩子節點的編號為`i`, 則其父節點的編號為`(i-1)//2`
 
## O(NLogN) Sift Up

```python
from typing import (
    List,
)

class Solution:
    
    def _siftUp(self, a: List[int], idx: int):
        while idx != 0:
            father_idx = (idx-1)//2
            if a[idx] > a[father_idx]:
                break
            a[idx], a[father_idx] = a[father_idx], a[idx]
            idx = father_idx

    def heapify(self, a: List[int]):
        """
        @param a: Given an integer array
        @return: nothing
        """
        for i in range(len(a)):
            self._siftUp(a, i)
```
#### Remark:
- 對於每個元素A[i]，比較A[i]和它的父親結點的大小，如果小於父親結點，則與父親結點交換。
- 交換後再和新的父親比較，重覆上述操作，直至該點的值大於父親。
#### Complexity:
- Time: O(NlogN)
  - 對於每個元素都要遍歷一遍，這部分是O(n)
  - 每處理一個元素時，最多需要向根部方向交換logn次。
- Space: O(1)

## O(N) Sift Down
```python
from typing import (
    List,
)

class Solution:

    def _siftDown(self, a: List[int], idx: int):
        """ Time: O(N) """
        while idx * 2 + 1 < len(a): # 至少有個左兒子
            son_idx = idx * 2 + 1 # a[i]左兒子的下標
            if idx * 2 + 2 < len(a) and a[son_idx] > a[idx * 2 + 2]:
                son_idx = idx * 2 + 2 # 選擇兩個兒子中較小的一個
            if a[son_idx] > a[idx]:
                break
                
            a[son_idx], a[idx] = a[idx], a[son_idx]
            idx = son_idx

    def heapify(self, a: List[int]):
        """
        @param a: Given an integer array
        @return: nothing
        """

        for i in range(len(a)//2, -1, -1):
            self._siftDown(a, i)
```
#### Remark:
- 初始選擇最接近葉子的一個父結點，與其兩個兒子中較小的一個比較，若大於兒子，則與兒子交換。
- 交換後再與新的兒子比較並交換，直至沒有兒子。
- 再選擇較淺深度的父親結點，重覆上述步驟。
#### Submission:
```
346 ms
time cost
·
18.95 MB
memory cost
·
Your submission beats
60.20 %
Submissions
```
#### Complexity:
- Time: O(N)
  - 這個版本的算法，乍一看也是 O(nlogn)， 但是我們仔細分析一下，算法從第 n/2 個數開始，倒過來進行 siftdown。也就是說，相當於從 heap 的倒數第二層開始進行 siftdown 操作，倒數第二層的節點大約有 n/4 個， 這 n/4 個數，最多 siftdown 1次就到底了，所以這一層的時間覆雜度耗費是 O(n/4)，然後倒數第三層差不多 n/8 個點，最多 siftdown 2次就到底了。所以這里的耗費是 O(n/8 * 2), 倒數第4層是 O(n/16 * 3)，倒數第5層是 O(n/32 * 4) ... 因此累加所有的時間覆雜度耗費為：
`T(n) = O(n/4) + O(n/8 * 2) + O(n/16 * 3)` ...
然後我們用 2T - T 得到 T(n):
```
2 * T(n) = O(n/2) + O(n/4 * 2) + O(n/8 * 3) + O(n/16 * 4) ...
T(n) = O(n/4) + O(n/8 * 2) + O(n/16 * 3) ...
2 * T(n) - T(n) = O(n/2) +O (n/4) + O(n/8) + ...
= O(n/2 + n/4 + n/8 + ... )
= O(n)
```
因此得到 T(n) = 2 * T(n) - T(n) = O(n)
- Space: O(1)

## Appendix: HeapSort
主要思想是通過把數組變成完全二叉樹來達到log(n)的目的。heapify的做法是每次確保i 大於 left 和 right。在排序的時候，利用了每次把最大的元素，放到size-1的位置上，然後再把size --。 heapify之後的數組並不是排序好的數組，只是能夠確保在log(n)的時間內，插入或者提取的最大數。
```python
class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        self._heapify(a=nums)
        for i in range(len(nums)-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self._siftDown(a=nums, idx=0, end=i-1)
        return nums

    def _siftDown(self, a: List[int], idx: int, end: int):

        while idx * 2 + 1 <= end: # 至少有個左兒子
            son_idx = idx * 2 + 1 # a[i]左兒子的下標
            if idx * 2 + 2 <= end and a[son_idx] < a[idx * 2 + 2]:
                son_idx = idx * 2 + 2 # 選擇兩個兒子中較大的一個
            if a[son_idx] < a[idx]:
                break

            a[son_idx], a[idx] = a[idx], a[son_idx]
            idx = son_idx

    def _heapify(self, a: List[int]):

        for i in range(len(a)-1//2, -1, -1):
            self._siftDown(a, i, len(a)-1)
```
