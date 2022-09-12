### Sort Colors II
https://www.lintcode.com/problem/143/
> Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.
<img src="../images/143_Sort-Colors-II.png" width="500px" />

```python
from typing import (
    List,
)

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing

    先整體有序 再局部有序
    """
    def sort_colors2(self, colors: List[int], k: int):
        if not colors or len(colors)<2: return
        self.partition_sort(colors, 1, k, 0, len(colors)-1)
    
    def partition_sort(self, colors: List[int], 
                       color_from: int, color_to: int, 
                       index_from: int, index_to: int):
        # base
        if color_from == color_to: return
        # recursive              
        mid_color = (color_from + color_to)//2 # division round down
        left, right = index_from, index_to
        while left <= right:
            while left <= right and colors[left] <= mid_color: # <= mid_color due to division round down
                left += 1
            while left <= right and colors[right] > mid_color:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left, right = left + 1, right - 1
        self.partition_sort(colors=colors, color_from=color_from, color_to=mid_color,
                                           index_from=index_from, index_to=right) #right=last idx of part 1
        self.partition_sort(colors=colors, color_from=mid_color+1, color_to=color_to,
                                           index_from=left, index_to=index_to) #left=first idx of part 2

```
#### Remark:
- for the right part recursive call, it's `color_from=mid_color+1`, not `color_from=mid_color`
- the colors are in order of 1, 2, ..., k, which does not start from zero
#### Submission:
```
103 ms
time cost
·
6.78 MB
memory cost
·
Your submission beats
45.00 %
Submissions
```
#### Complexity:
- Time: O(nlogk) where n=length of arrays and k=number of colors
- Space: O(logk)
