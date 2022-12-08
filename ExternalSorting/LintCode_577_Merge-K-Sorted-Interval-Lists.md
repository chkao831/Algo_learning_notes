### Merge K Sorted Interval Lists
https://www.lintcode.com/problem/577/
> Merge K sorted interval lists into one sorted interval list. You need to merge overlapping intervals too.
```python
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from typing import List, Tuple
from heapq import heappush, heappop

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """

    def _merge_tuple_to_output(self, tup: Interval, output_list: List[Interval]) -> List[Interval]:
        if not output_list or output_list[-1].end < tup.start:
            output_list.append(tup)
        else:
            output_list[-1].end = max(output_list[-1].end, tup.end)
        return output_list

    def mergeKSortedIntervalLists(self, intervals):
        if not intervals:
            return None
        heap = []
        for idx_arr, interval_list in enumerate(intervals):
            if not interval_list:
                continue
            tup = (interval_list[0].start, interval_list[0].end)
            heappush(heap, (tup, idx_arr, 0))
        output_list = []
        while heap:
            (popped_tup, idx_arr, idx_order) = heappop(heap)
            popped_interval = Interval(popped_tup[0], popped_tup[1])
            output_list = self._merge_tuple_to_output(popped_interval, output_list)
            if idx_order+1 < len(intervals[idx_arr]):
                tup = (intervals[idx_arr][idx_order+1].start, intervals[idx_arr][idx_order+1].end)
                heappush(heap, (tup, idx_arr, idx_order+1))
        return output_list

```
#### Remark:
- `def _merge_tuple_to_output` 完全同[Lint839 - Merge Two Sorted Interval Lists](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_839_Merge-Two-Sorted-Interval-Lists.md)
- 需要注意：
  - heap的元素由(interval的內容, 是在第幾個array, 是在該array排第幾個位子）組成
  - interval的內容是一個`Tuple`，為了能夠comparable，要特意從`Interval`轉成`Tuple`再push to heap
  - 不過，`Tuple`並不mutable，為了配合 `def _merge_tuple_to_output` 中mutable的`Interval`(終區間必須要可以彈性轉換)，進去該函數前要轉回`Interval`
#### Submission:
```
1019 ms
time cost
·
12.63 MB
memory cost
·
Your submission beats
7.20 %
Submissions
```
#### Complexity:
- Time: O(NlogK)
- Space: O(K)
