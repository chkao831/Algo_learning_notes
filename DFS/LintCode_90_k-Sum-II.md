### k Sum II
https://www.lintcode.com/problem/90/description
>Given n distinct positive integers, the integer k and a target number.
>
>Find k distinct numbers within these n numbers such that the sum of these k numbers equals the target number, and you need to find all the solutions that satisfy the requirement (the order of the solutions is not required).
```python
from typing import List

class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A: List[int], k: int, target: int) -> List[List[int]]:

        def dfs(startingIndex: int, curr_k: int, t: int, subset: List[int]):

            if curr_k == k:
                if t==0:
                    subsets.append(list(subset)) 
                return
            for i in range(startingIndex, len(A)):
                subset.append(A[i])
                dfs(i + 1, curr_k + 1, t - A[i], subset)
                subset.pop()

        A.sort()
        subsets = []
        dfs(startingIndex=0, curr_k=0, t=target, subset=[])
        return subsets
```
#### Remark:
- 和Lint135不同的在於
  - 每個數不能選兩次了，進來的數也已經都是distinct
  - 需要加一個counter去算目前幾個k了 
#### Submission:
```
608 ms
time cost
·
6.12 MB
memory cost
·
Your submission beats
37.60 %
Submissions
```
#### Complexity:
- Time: 
- Space: O(1) (遞歸深度=2)
