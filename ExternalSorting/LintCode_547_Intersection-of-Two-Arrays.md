# Intersection of Two Arrays
https://www.lintcode.com/problem/547/
>
## 1. python build-in

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
#### Remark:
- 
#### Submission:
```
```
#### Complexity:
- Time: O(m+n)，其中 m 和 n 分別是兩個數組的長度。使用兩個集合分別存儲兩個數組中的元素需要O(m+n)的時間，遍歷較小的集合併判斷元素是否在另一個集合中需要O(min(m,n))的時間，因此總時間複雜度是O(m+n)。
- Space: O(m+n)

## 2. sort + two pointers

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        length1, length2 = len(nums1), len(nums2)
        intersection = list()
        index1 = index2 = 0
        while index1 < length1 and index2 < length2:
            num1 = nums1[index1]
            num2 = nums2[index2]
            if num1 == num2:
                # 保证加入元素的唯一性
                if not intersection or num1 != intersection[-1]:
                    intersection.append(num1)
                index1 += 1
                index2 += 1
            elif num1 < num2:
                index1 += 1
            else:
                index2 += 1
        return intersection
```
#### Remark:
- 
#### Submission:
```
```
#### Complexity:
- Time: O(mlogm+nlogn)
- Space: O(1)

## 3. Sort + Merge

```python
from typing import (
    List,
)

class Solution :
    # *
    #     * @param nums1 ana integer array
    #     * @param nums2 an integer array
    #     * @return an integer array
    def intersection(self, nums1,  nums2) :
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        temp = [0] * (len(nums1))
        index = 0
        while (i < len(nums1) and j < len(nums2)) :
            if (nums1[i] == nums2[j]) :
                if (index == 0 or temp[index - 1] != nums1[i]) :
                    temp[index] = nums1[i]
                    index += 1
                i += 1
                j += 1
            elif(nums1[i] < nums2[j]) :
                i += 1
            else :
                j += 1
        result = [0] * (index)
        k = 0
        while (k < index) :
            result[k] = temp[k]
            k += 1
        return result
```
#### Remark:
- 
#### Submission:
```
```
#### Complexity:
- Time: O(mlogm+nlogn)
- Space: O(1)

## 4. Sort + Binary Search

```python
from typing import (
    List,
)

class Solution :
    # *
    #     * @param nums1 ana integer array
    #     * @param nums2 an integer array
    #     * @return an integer array
    def intersection(self, nums1, nums2):
        # idea: binary search + hash set
        result = set()
        if len(nums1) > len(nums2):
            s_nums = nums2
            b_nums = nums1
        else:
            s_nums = nums1
            b_nums = nums2

        s_nums.sort()
        for num in b_nums:
            if self.binary_seach(s_nums, num):
                result.add(num)
        return list(result)


    def binary_seach(self, nums, target):
        if not nums or len(nums) == 0:
            return False

        start, end = 0, len(nums) -1
        while start + 1 < end:
            middle = start + (end - start) // 2

            if nums[middle] <= target:
                start = middle
            elif nums[middle] > target:
                end = middle

        if nums[end] == target or nums[start] == target:
            return True
        return False
```
#### Remark:
- 
#### Submission:
```
```
#### Complexity:
- Time: O(nlogn) where n = len(bigger_array)
- Space: O(1)
