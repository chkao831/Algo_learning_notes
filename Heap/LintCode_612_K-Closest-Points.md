# K Closest Points
https://www.lintcode.com/problem/612/description
>在二維空間里給定一些 points 和一個 origin，從 points 中找到 k 個離 origin 歐幾里得距離最近的點。按照歐幾里得距離由小到大返回。如果兩個點有相同歐幾里得距離，則按照x值來排序；若x值也相同，就再按照y值排序。

Very similar to [Lint545 - Top k Largest Numbers II](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LintCode_545_Top-k-Largest-Numbers-II.md)  

## Quick Select + Sort Top K = O(n + klogk)
```python
from typing import (
    List, Tuple
)
from lintcode import (
    Point,
)
from math import sqrt

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def k_closest(self, points: List[Point], origin: Point, k: int) -> List[Point]:

        def _calc_distance(target: Point, pt: Point) -> Tuple:
            dis = sqrt((target.x-pt.x)**2 + (target.y-pt.y)**2)
            return (dis, pt.x, pt.y)

        def _quickSelect(list_distance: List[Tuple], start: int, end: int, k: int):
            if start >= end:
                return
            left, right = start, end
            pivot = list_distance[(left+right)//2]
            while left <= right:
                while left <= right and list_distance[left] < pivot:
                    left += 1
                while left <= right and list_distance[right] > pivot:
                    right -= 1
                if left <= right:
                    list_distance[left], list_distance[right] = list_distance[right], list_distance[left]
                    left, right = left + 1, right - 1
            if k <= right:
                _quickSelect(list_distance=list_distance, start=start, end=right, k=k)
            if k >= left:
                _quickSelect(list_distance=list_distance, start=left, end=end, k=k)

        # generate list of tuple (distanceToOrigin, x_coord, y_coord), O(N)
        list_distanceTuple = []
        for point in points:
            list_distanceTuple.append(_calc_distance(origin, point))

        # quick select, O(N)
        _quickSelect(list_distance=list_distanceTuple, start=0, end=len(list_distanceTuple)-1, k=k-1)
        top_k = list_distanceTuple[:k]
        
        # sort top k, O(klogk)
        top_k.sort()
        output_list = []
        for pt in top_k: # O(k)
            output_list.append(Point(pt[1], pt[2]))
        return output_list
```
#### Remark:
- Trick: 使用含有多個元素的tuple or list比大小 (e.g. `(3,1,5) > (2,6,8)`)
- 記住！Quick Select跟pivot比時，是`>, <`不是`>=, <=`
- 取二次方是`**2`不是`^2`、取根號要`import math` 然後`sqrt()`
- 可以用list comprehension縮行
    ```python
    output_list = []
    for pt in top_k:
        output_list.append(Point(pt[1], pt[2]))
    ``` 
    to
    ```python
    list(Point(x,y) for (_,x,y) in top_k)
    ```
- 可以用list comprehension縮行
    ```python
    def _calc_distance(target: Point, pt: Point) -> Tuple:
        dis = sqrt((target.x-pt.x)**2 + (target.y-pt.y)**2)
        return (dis, pt.x, pt.y)
            
    list_distanceTuple = []
    for point in points:
        list_distanceTuple.append(_calc_distance(origin, point))
    ``` 
    to
    ```python
    list_distanceTuple = [(sqrt((target.x-pt.x)**2 + (target.y-pt.y)**2), point.x, point.y) for point in points]
    ```
- 在k比n小很多的時候，比Heap的方法優。`O(n+klogk) << O(nlogk) when k << n`; k,n差不多時，時間複雜度相當。
#### Submission:
```
990 ms
time cost
·
38.15 MB
memory cost
·
Your submission beats
21.20 %
Submissions
```
#### Complexity:
- Time: O(n + klogk)
- Space: O(n) (`list_distanceTuple`)

## Heap = O(nLogk)
```python
from typing import (
    List, Tuple
)
from lintcode import (
    Point,
)
from math import sqrt
from heapq import heappush, heappop

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def k_closest(self, points: List[Point], origin: Point, k: int) -> List[Point]:
        heap = [] # maxheap
        for point in points: # O(NlogK)
            heappush(heap, (-sqrt((origin.x-point.x)**2 + (origin.y-point.y)**2), -point.x, -point.y))
            if len(heap) > k:
                heappop(heap)
        list_out = []

        # O(KlogK)
        while heap: # for _ in range(len(heap)):
            _, x, y = heappop(heap)
            list_out.append(Point(-x, -y))
        list_out.reverse()
        return list_out
```
#### Remark:
- 雖然乍看是找最近的點，minHeap，會耗費O(nlogn)的時間。但是可以換一個角度想，要取K個最近的點，可以維護K個點的heap就好。
- =>使用maxHeap，當堆裡超過k個元素時，pop掉最大的（距離最遠的）。時間複雜度為O(nlogk)。
- 在k比n小很多的時候，劣於QuickSelect的方法。`O(n+klogk) << O(nlogk) when k << n`; k,n差不多時，時間複雜度相當。

#### Submission:
```
915 ms
time cost
·
35.95 MB
memory cost
·
Your submission beats
47.80 %
Submissions
```
#### Complexity:
- Time: O(nlogk)
- Space: O(n)

# Summary
| Offline version - Find Closest (find smallest) | Quick Select | MinHeap | MaxHeap |
|---|---|---|---|
| TopK | O(n+klogk) | O(nlogn) | O(nlogk) |
| Rank | Better when n >> k | Worst | Comparably good when n~k |