### Subsets II
https://www.lintcode.com/problem/18/
> Given a collection of integers that might contain duplicate numbers, return all possible subsets.\
> **The solution set must not contain duplicate subsets.**

Link to [Subsets-I](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_17_Subsets.md)

```python
from typing import (
    List,
)

class Solution:
    
    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        """
        @param nums: A set of numbers.
        @return: A list of lists. All valid subsets.
                we will sort your return value in output
        """

        def dfs(index: int, subset: List[int]):

            # base: add every combo in the current subset to the returning result
            result.append(list(subset))
            # if there's subsequent index, do recursive call
            for i in range(index, len(nums)):
                if (i>index and nums[i]==nums[i-1]):
                    continue
                subset.append(nums[i])
                dfs(i+1, subset)
                subset.pop() # backtracking

        result = []
        if not nums:
            return [[]]
        nums.sort() # because elements in a subset must be in non-descending order
        dfs(index=0, subset=[])
        return result

```
#### Remark:
- 選代表：為了避免重複
```
{1, 2, 2} 
    ^
  選這個
```
在for循環內部 在每一個index都去看看跟相鄰的前面有沒有一樣
在組合問題裡，是為了避免 `nums = [1,2,2]` 的input, 給出
```
[
  [2],
  [2], <- 這種重複的答案
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```
#### Submission:
```
102 ms
time cost
·
6.25 MB
memory cost
·
Your submission beats
46.40 %
Submissions
```
#### Complexity:
- Time: O(n*2^n)
- Space: O(n)
