### Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/
>Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
>
>An integer a is closer to x than an integer b if:
>```
>|a - x| < |b - x|, or
>|a - x| == |b - x| and a < b
>```

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        def binary_search() -> int:
            start, end = 0, len(arr) - 1
            while start + 1 < end:
                mid = (start + end)//2
                if arr[mid] < x:
                    start = mid
                else:
                    end = mid
            if arr[start] >= x: return start
            if arr[end] >= x: return end
            return len(arr) # not found
        
        def left_closer(right: int, left: int) -> bool:
            if left < 0: # must be right closer
                return False
            if right >= len(arr): # must be left closer
                return True
            return True if x - arr[left] <= arr[right] - x else False
        
        right = binary_search()
        left = right - 1
        for _ in range(k):
            if left_closer(right, left):
                left -= 1
            else:
                right += 1
        return arr[left+1:right]
```
#### Remark:
- Similar to [Lint460](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_460_Find-K-Closest-Elements.md), except that upon returning, use pointer to control the interval to be returned, since the result should be sorted in ascending order.
  ```
     [1, 2, 3, 4, 5], return [2, 3]
      ^        ^
     [1, 2, 3, 4, 5], return [1, 2]
   ^        ^ 
  return: left pointer and right pointer exclusive
  ```
#### Submission:
```
Runtime: 320 ms, faster than 90.81% of Python3 online submissions for Find K Closest Elements.
Memory Usage: 15.6 MB, less than 27.41% of Python3 online submissions for Find K Closest Elements.
```
#### Complexity:
- Time: O(logn) + O(k)
- Space: O(1)
