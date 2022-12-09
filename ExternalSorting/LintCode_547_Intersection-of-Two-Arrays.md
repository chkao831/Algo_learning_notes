# Intersection of Two Arrays
https://www.lintcode.com/problem/547/
>Given two arrays, write a function to compute their intersection.
## 1. Python build-in

```python
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
             we will sort your return value in output
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection((set(nums2))))
```
#### Submission:
```
344 ms
time cost
·
32.03 MB
memory cost
·
Your submission beats
67.80 %
Submissions
```
#### Complexity:
空間複雜度劣於下面兩種方法，但是時間複雜度較優秀。
- Time: O(m+n)，其中 m 和 n 分別是兩個數組的長度。使用兩個集合分別存儲兩個數組中的元素需要O(m+n)的時間，遍歷較小的集合併判斷元素是否在另一個集合中需要O(min(m,n))的時間，因此總時間複雜度是O(m+n)。
- Space: O(m+n)

## 2. Two In-place Sorts + Two Pointers (數組合併)

```python
from typing import List

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
                if not list_out or num1 != list_out[-1]:
                    list_out.append(num1)
                ptr_1, ptr_2 = ptr_1 + 1, ptr_2 + 1
            elif num1 < num2:
                ptr_1 += 1
            else:
                ptr_2 += 1
        return list_out
```
#### Remark:
- 運用數組合併技巧，優點是除了雙指針，沒有額外空間，但先前的sort in place時間複雜度可能會是bottleneck
#### Submission:
```
588 ms
time cost
·
26.55 MB
memory cost
·
Your submission beats
41.40 %
Submissions
```
#### Complexity:
- Time: O(mlogm+nlogn)
- Space: O(1)

## 3. One In-place Sort + Binary Search

```python
from typing import List

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
             we will sort your return value in output
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        def _binary_search_in_smaller_arr(small_arr: List[int], target_num: int) -> bool:
            left, right = 0, len(small_arr)-1
            while left + 1 < right:
                mid = (left + right)//2
                if small_arr[mid] >= target_num:
                    right = mid
                else:
                    left = mid
            if small_arr[right] == target_num or small_arr[left] == target_num:
                return True
            return False

        if not nums1 or not nums2:
            return []

        if len(nums1) <= len(nums2):
            small_arr, big_arr = nums1, nums2
        else:
            small_arr, big_arr = nums2, nums1
        set_intersection = set()
        small_arr.sort()
        for big in big_arr:
            if _binary_search_in_smaller_arr(small_arr, big):
                set_intersection.add(big)
        return list(set_intersection)
```
#### Remark:
- 為什麼要選小的sort in-place, 然後for loop大的數組找小的裡面有沒有？
    - if #小 = 2, #大 = 3,
        - 小的sort, for大 => 2log2 + 3log2 = 5log2 (better)
        - 大的sort, for小 => 3log3 + 2log3 = 5log3
- [Binary Search 模板](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_457_Classical-Binary-Search.md)

#### Submission:
```
1383 ms
time cost
·
26.92 MB
memory cost
·
Your submission beats
10.40 %
Submissions
```
#### Complexity:
和第二種方法相當：
- Time: O(nlogn) where n = len(bigger_array)
- Space: O(1)
