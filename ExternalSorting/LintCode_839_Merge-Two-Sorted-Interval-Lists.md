### Merge Two Sorted Interval Lists
https://www.lintcode.com/problem/839/description
>Merge two sorted (ascending) lists of interval and return it as a new sorted list. The new sorted list should be made by splicing together the intervals of the two lists and sorted in ascending order.\
>**The intervals in the given list do not overlap; The intervals in different lists may overlap.**
```python
from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def merge_two_interval(self, list1: List[Interval], list2: List[Interval]) -> List[Interval]:

        def _merge_tuple_to_output(tup: Interval, output_list: List[Interval]) -> List[Interval]:
            if not output_list or output_list[-1].end < tup.start:
                output_list.append(tup)
            else:
                output_list[-1].end = max(output_list[-1].end, tup.end)
            return output_list

        output_list = []
        l1_ptr, l2_ptr = 0, 0
        while l1_ptr < len(list1) and l2_ptr < len(list2):
            num1, num2 = list1[l1_ptr], list2[l2_ptr]
            if (num1.start <= num2.start):
                output_list = _merge_tuple_to_output(tup=num1, output_list=output_list)
                l1_ptr += 1
            else: # num1.start > num2.start
                output_list = _merge_tuple_to_output(tup=num2, output_list=output_list)
                l2_ptr += 1
        while l1_ptr < len(list1):
            output_list = _merge_tuple_to_output(tup=list1[l1_ptr], output_list=output_list)
            l1_ptr += 1
        while l2_ptr < len(list2):
            output_list = _merge_tuple_to_output(tup=list2[l2_ptr], output_list=output_list)
            l2_ptr += 1
        return output_list
```
#### Remark:
- Merge主要邏輯都還是採用[Lint165](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_165_Merge-Two-Sorted-Lists.md)等題衍生的數組合併技巧
- 在merge tuple時，之所以可以修改：`output_list[-1].end = max(output_list[-1].end, tup.end)`，是因為這個tuple不是Tuple，而是`Interval` object，如果沒有這個object輔助，要用list才mutable
#### Submission:
```
101 ms
time cost
·
5.93 MB
memory cost
·
Your submission beats
85.40 %
Submissions
```
#### Complexity:
- Time: O(m+n)
- Space: O(1)
