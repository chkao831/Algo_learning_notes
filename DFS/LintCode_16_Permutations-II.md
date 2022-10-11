### Permutations II
https://www.lintcode.com/problem/16/
>Given a list of numbers **with duplicate numbers** in it, find all **unique permutations** of it.

Link to [Permutations-I](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_15_Permutations.md)

```python
from typing import (
    List, Set
)

class Solution:
    """
    @param nums: A list of integers
    @return: A list of unique permutations
             we will sort your return value in output
    """
    def permute_unique(self, nums: List[int]) -> List[List[int]]:

        def dfs(subset: List[int], visited: List[bool]):
            # base
            if len(subset) == len(nums):
                result.append(list(subset)) # this takes O(n)!!! (構建每個方案deepcopy進去的時間)
                return

            # recursive
            for idx, num in enumerate(nums):
                if visited[idx]:
                    continue
                # [1, 2, 2, 2, 3] 選第二、第三個二的時候，要確保前面的二已經被選了
                if idx > 0 and nums[idx] == nums[idx-1] and visited[idx - 1]: # not visited[idx-1]表跳過前面的重複數了，不行
                    continue
                subset.append(num)
                visited[idx] = True
                dfs(subset, visited)
                subset.pop()
                visited[idx] = False

        result = []
        if not nums:
            return [[]]
        nums.sort() # because we're given a list of numbers with duplicate numbers in it
        dfs(subset=[], visited=[False for i in range(0, len(nums))])
        return result

```
#### Remark:
- 為了把重複的數集中管理，需要排序了 `nums.sort()`
- 和Permutations-I相似，也需要visited去管理已經經過的數字
  - 但是，不再用`set()`，因為此題可能有duplicated number, 需要計入, 把他們當不同的數
  - 用`visited` **list** 管理，用位置(index)判斷
    - `visited=[False for i in range(0, len(nums))]`
  - 以`[1, 2, 2, 2, 3]`為例，選第二、第三個二的時候，要確保前面的二已經被選了
    - `if visited[idx-1]: continue` 
#### Submission:
```
102 ms
time cost
·
6.00 MB
memory cost
·
Your submission beats
40.20 %
Submissions
```
#### Complexity:
- Time: O(方案總數 * 構造每個方案的時間) = O(n! * n)
- Space: O(n) (for subset list and visited list)
