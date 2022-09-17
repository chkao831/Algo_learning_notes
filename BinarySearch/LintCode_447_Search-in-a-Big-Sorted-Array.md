 ### Search in a Big Sorted Array
 https://www.lintcode.com/problem/447/
 
 >Given a big sorted array with non-negative integers sorted by non-decreasing order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).
>
>Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.
>
>Return -1, if the number doesn't exist in the array.
>
 #### 倍增法 (Exponential Backoff，指數回退)
 ```
 [ 0, 1, 2, 3, ..., k, ...]
                    ^
                  target
```
To find the target in log(k) time, try Exponential Backoff.\
Similar scenarios that apply Exponential Backoff: ArrayList in Java, vector in C++, 網路重試, etc.\
Worst Scenario: **O(log(2k-2)) = O(log(k))**
```
1 -> 2 -> 4 -> 8 -> ... -> k-1 -> 2k-2
 [ 0, 1, 2, 3, ...k-1, k, ...]
                   ^
                 stop here
                 then next time to
 [ 0, 1, 2, 3, ...k-1, k, ..., 2k-2]                
```

#### Code
```python
class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        kth = 1
        # Exponential Backoff
        while reader.get(kth-1) < target:
            kth *= 2
        # Binary Search
        start, end = 0, kth-1
        while start + 1 < end:
            mid = (start + end)//2
            if reader.get(mid) == target:
                end = mid
            elif reader.get(mid) < target:
                start = mid
            else: # reader.get(mid) > target
                end = mid
        if reader.get(start) == target: return start
        if reader.get(end) == target: return end
        return -1
```
#### Remark:
#### Submission:
```
305 ms
time cost
·
57.96 MB
memory cost
·
Your submission beats
66.20 %
Submissions
```
#### Complexity:
- Time: O(logn)
- Space: O(1)

