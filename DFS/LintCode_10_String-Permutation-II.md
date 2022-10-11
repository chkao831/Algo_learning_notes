### String Permutation II
https://www.lintcode.com/problem/10/
>Given a string, find all permutations of it **without duplicates**.
```python
from typing import (
    List,
)

class Solution:
    """
    @param str: A string
    @return: all permutations
             we will sort your return value in output
    """
    def string_permutation2(self, str: str) -> List[str]:

        def dfs(subset: List[int], visited: List[bool]):
            if len(subset) == len(list_str):
                result.append(''.join([ele for ele in subset]))
                return
            for idx, val in enumerate(list_str):
                if visited[idx]:
                    continue
                if idx>0 and list_str[idx-1]==list_str[idx] and not visited[idx-1]:
                    continue
                subset.append(val)
                visited[idx] = True
                dfs(subset, visited)
                subset.pop()
                visited[idx] = False
    
        result = []
        if not str:
            return [""]
        list_str = list(str)
        list_str.sort()
        dfs(subset=[], visited=[False for i in range(len(list_str))])
        return result
```
#### Remark:
- Very similar to [Lint16-PermutationsII](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_16_Permutations-II.md), except that need to convert `str` to `list` first, then convert back before appending to result. 
- `str` is immutable, 中間處理不要用string concatenation (e.g. `str1 + str2`) 傳進去dfs recursive call, 用list append
#### Submission:
```
2093 ms
time cost
·
38.20 MB
memory cost
·
Your submission beats
10.80 %
Submissions
```
#### Complexity:
- Time: O(方案總數 * 構造每個方案的時間) = O(n! * n), n=字符總數
- Space: O(n)
