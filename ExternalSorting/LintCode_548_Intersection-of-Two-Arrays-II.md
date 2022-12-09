# Intersection of Two Arrays II
https://www.lintcode.com/problem/548/
>

## 1. Hashmap (Counter)
```python
from typing import (
    List,
)
from collections import Counter

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
             we will sort your return value in output
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums1)
        output_list = []
        for num in nums2:
            if counter[num] > 0:
                output_list.append(num)
                counter[num] -= 1
        return output_list
```
#### Remark:
- 用dict維護前一個數組中每個值出現的次數，然後遍歷第二個數組，對於每個遍歷到的數，在dict中將這個數出現的次數-1
- 空間複雜度劣於下面的方法，但是時間複雜度較優秀。
#### Submission:
```
424 ms
time cost
·
31.93 MB
memory cost
·
Your submission beats
77.00 %
Submissions
```
#### Complexity:
- Time: O(m+n)
- Space: O(m), where m=len(nums1)

## 2. Two In-place Sorts + Two Pointers (數組合併)
```python
from typing import (
    List,
)
from collections import Counter

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
             we will sort your return value in output
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ptr_1, ptr_2 = 0, 0
        list_out = []
        while ptr_1 < len(nums1) and ptr_2 < len(nums2):
            num1, num2 = nums1[ptr_1], nums2[ptr_2]
            if num1 == num2:
                list_out.append(num1)
                ptr_1, ptr_2 = ptr_1 + 1, ptr_2 + 1
            elif num1 < num2:
                ptr_1 += 1
            else:
                ptr_2 += 1
        return list_out
```
#### Remark:
- 運用數組合併技巧，優點是除了雙指針，沒有額外空間，但sort in place時間複雜度可能會是bottleneck
- 和[Lint547-Intersions I](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_547_Intersection-of-Two-Arrays.md#2-two-in-place-sorts--two-pointers-%E6%95%B8%E7%B5%84%E5%90%88%E4%BD%B5)幾乎一模一樣，除了這裡允許duplication，少了一句if statement: `if not list_out or num1 != list_out[-1]: list_out.append(num1)`
#### Submission:
```
634 ms
time cost
·
26.54 MB
memory cost
·
Your submission beats
21.00 %
Submissions
```
#### Complexity:
- Time: O(mlogm+nlogn)
- Space: O(1)

### 註：不能用[Lint547-Intersions I](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_547_Intersection-of-Two-Arrays.md#3-one-in-place-sort--binary-search)裡面的binary search方法，因為這題需要duplication，binary search一個個找缺少標記方法。
