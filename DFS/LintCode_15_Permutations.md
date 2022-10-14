# Permutations
https://www.lintcode.com/problem/15/  
> Given a list of numbers, return all possible permutations of it.

## DFS: Recursive Approach
```python
from typing import (
    List, Set
)

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
             we will sort your return value in output
    """
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(subset: List[int], visited: Set):
            # base
            if len(subset) == len(nums):
                result.append(list(subset)) # this takes O(n)!!! (構建每個方案deepcopy進去的時間)
                return

            # recursive
            for num in nums:
                if num in visited:
                    continue
                subset.append(num)
                visited.add(num)
                dfs(subset, visited)
                subset.pop()
                visited.remove(num)

        result = []
        if not nums:
            return [[]]
        dfs(subset=[], visited=set())
        return result
```

#### Remark:
- 因為順序無關了，只有一個限制：一個樹不能重複用兩次（用`set()`)
  - base case: 長度和原數組相同時返回，同時必須對小數組進行deepcopy，否則出最後的dfs的時候會出現全部空集（全部都backtracking回最原本的東西了）
    - 核心：`append()` or `pop()` 這些操作都是不改變內存地址的，可以用`id(...)`看出來 
  - backtracking要記得也要改visited set
    - 但其實`remove(num)`就不能保證O(1)時間複雜度了 
- Time
  - O(n! * n)
- 遞歸三要素
  - 定義：找到所有以permutation為開頭的permutations
  - 出口：長度和原數組相同時
  - 拆解：`[] -> [1][2][3], [1] -> [1,2][1,3], ...`
- Mistake:
  - `set()`是沒有排序的（`list()`有），所以backtracking on set不可以`visited.pop()`, 要`visited.remove(num)`!!! 
#### Submission:
```
102 ms
time cost
·
6.06 MB
memory cost
·
Your submission beats
37.20 %
Submissions
```
#### Complexity:
- Time: O(方案總數 * 構造每個方案的時間) = O(n! * n)
- Space: O(n) (for subset list and visited set)

## DFS: 非遞歸的方式實現排列和組合類DFS
Based on [Leet 31 - Next Permutation](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_31_Next-Permutation.md)
```python
from typing import (
    List, Set
)

class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(idx1: int, idx2: int):
            nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
            return
    
        def reverse(startingIndex: int):
            left, right = startingIndex, len(nums)-1
            while left < right:
                swap(left, right)
                left, right = left+1, right-1
            return
        
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # i is at the first decreasing index
        if i < 0: 
            return False
        else: # i >= 0
            j = len(nums) - 1
            while nums[i] >= nums[j]:
                j -= 1
            swap(i, j)
        reverse(i+1)
        return True

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        @param nums: A list of integers.
        @return: A list of permutations.
                we will sort your return value in output
        """
        
        nums.sort()
        result = []
        hasNext = True
        while hasNext:
            result.append(list(nums))
            hasNext = self.nextPermutation(nums)
        return result
```
#### Remark:
- [Next Permutation](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_31_Next-Permutation.md):
    - Q: i為0怎麼辦？
        - A: i為0說明整個數組是降序的，直接翻轉整個數組即可。 
    - Q: 有重復元素怎麼辦？
        - A: 在遍歷時只要嚴格滿足 nums[i] > nums[i - 1] 和 nums[j] > nums[i - 1] 就不會有問題。 
    - Q: 元素過少是否要單獨考慮？
        - A: 當元素個數小於等於1個時，可以直接返回。
#### Submission:
```
101 ms
time cost
·
6.01 MB
memory cost
·
Your submission beats
68.20 %
Submissions
```
#### Complexity:
- Time: O(num_of_next_permutations * n)
- Space: O(n)
