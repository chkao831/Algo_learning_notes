### Classical Binary Search
https://www.lintcode.com/problem/457/description
>Find any position of a target number in a sorted array. Return -1 if target does not exist.
```python
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        if not nums:
            return -1

        start, end = 0, len(nums)-1
        while start+1 < end: # avoid dead cycle
            mid = (start+end)//2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target: # go up
                start = mid
            else: # nums[mid] > target, go down
                end = mid 
        # start, end off by 1, need to judge
        if nums[start] == target:
            return start
        if nums[end] == target: # if searching for last position, shift this up
            return end
        return -1
```
#### Remark:
- For finding first position where a number shows up, it's the same question as above.
#### Submission:
```
1299 ms
time cost
·
41.75 MB
memory cost
·
Your submission beats
40.80 %
Submissions
```
#### Complexity:
- Time: O(logn)
- Space: O(1)
