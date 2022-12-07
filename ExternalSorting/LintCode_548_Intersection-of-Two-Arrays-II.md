# Intersection of Two Arrays II
https://www.lintcode.com/problem/548/
>

## 1. Hash
```python
class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # Write your code here
        counts = collections.Counter(nums1)
        result = []

        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result
```
#### Remark:
- 用dict维护前一个数组中每个值出现的次数
然后遍历第二个数组，对于每个遍历到的数，在dict中将这个数出现的次数-1
#### Submission:
```
```
#### Complexity:
- Time: O(m+n)
- Space: O(m)

## 2. Sort + Merge
```python
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        p1, p2 = 0, 0
        result = []
        while p1 != len(nums1) and p2 != len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums2[p2] < nums1[p1]:
                p2 += 1
            else:
                result.append(nums1[p1])
                p1 += 1
                p2 += 1
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

## 3. Two pointers
```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        length1, length2 = len(nums1), len(nums2)
        intersection = list()
        index1 = index2 = 0
        while index1 < length1 and index2 < length2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                intersection.append(nums1[index1])
                index1 += 1
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
