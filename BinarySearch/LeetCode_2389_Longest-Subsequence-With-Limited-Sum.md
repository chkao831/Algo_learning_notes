## Longest Subsequence With Limited Sum
https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/
>You are given an integer array nums of length `n`, and an integer array queries of length `m`.
>
>Return an array answer of length `m` where `answer[i]` is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to `queries[i]`.



### PrefixSum + BinarySearch (written)
```python
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        def _binary_search(target: int, arr: List[int]) -> int:
            start, end = 0, len(arr)-1
            while start + 1 < end:
                mid = (start + end) //2
                if arr[mid] <= target:
                    start = mid
                else:
                    end = mid
            if arr[end] <= target: # last position of target
                return end
            if arr[start] <= target:
                return start
            return -1
        
        # in-place sort + prefixSum: O(NlogN)
        nums.sort()
        prefixSum = [0]*len(nums)
        prefixSum[0] = nums[0]
        for idx in range(1, len(nums)):
            prefixSum[idx] = prefixSum[idx-1] + nums[idx]
        # for each q in queries, binary search within prefixSum: O(MlogN)
        ans = []
        for q in queries:
            ans_idx = _binary_search(q, prefixSum)
            ans.append(ans_idx+1)
        return ans
```
#### Remark:
- Last position of target: https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_458_Last-Position-of-Target.md
- 手刻binary search:
  - 要回傳last position of target
  - 回傳的是：在prefixSum array裡，直至哪個index還是小於等於目標值
  - 和bisest的區別：因為是回傳原array的pointer index, 所以最後出來的值要加一，才是subsequence的長度
  - edge case: 如果是-1 (根本沒有一個數比目標值小），加一也沒錯（回0)
#### Submission:
```
Runtime
124 ms
Beats
88.83%

Memory
14.2 MB
Beats
79.61%
```
### PrefixSum + BinarySearch (written)
```python
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        # in-place sort + prefixSum: O(NlogN)
        nums.sort()
        prefixSum = [0]*len(nums)
        prefixSum[0] = nums[0]
        for idx in range(1, len(nums)):
            prefixSum[idx] = prefixSum[idx-1] + nums[idx]
        # for each q in queries, binary search within prefixSum: O(MlogN)
        ans = []
        for q in queries:
            ans_idx = bisect.bisect_right(prefixSum, q)
            ans.append(ans_idx)
        return ans
```
#### Remark:
- `bisect`: 透過二元搜尋的方式，插入元素到串列之中
  -  `bisect.bisect_left` 所回傳的串列索引位置會確保該位置左邊都<欲插入的值，而該位置右邊的所有值都>=欲插入的值 (equiv. to first position)
  -  `bisect.bisect_right` or `bisect.bisect` 所回傳的串列索引位置會確保該位置左邊都<=欲插入的值，而該位置右邊的所有值都>欲插入的值 (equiv. to last position)
  -  和手刻版本的區別是，因為是回傳插入以後的那個位置，所以不用+1
#### Submission:
```
Runtime
91 ms
Beats
99.90%

Memory
14.1 MB
Beats
79.61%
```

### Complexity:
- Time: O(nlogn + mlogn)
- Space: O(n)
