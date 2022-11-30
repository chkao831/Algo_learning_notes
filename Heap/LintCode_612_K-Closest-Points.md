# K Closest Points
https://www.lintcode.com/problem/612/description
>在二維空間里給定一些 points 和一個 origin，從 points 中找到 k 個離 origin 歐幾里得距離最近的點。按照歐幾里得距離由小到大返回。如果兩個點有相同歐幾里得距離，則按照x值來排序；若x值也相同，就再按照y值排序。

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
- []比大小
- pivot > < not >= <=
- abbr
    ```python
    output_list = []
    for pt in top_k:
        output_list.append(Point(pt[1], pt[2]))
    ``` 
    to
    ```python
    list(Point(x,y) for (_,x,y) in top_k)
    ```
- abbr
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
