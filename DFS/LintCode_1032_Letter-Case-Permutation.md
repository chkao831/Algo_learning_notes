### Letter Case Permutation
https://www.lintcode.com/problem/1032/
>Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string. Return a list of all possible strings we could create.
```python
from typing import (
    List,
)
from collections import deque

class Solution:
    """
    @param s: a string
    @return: return a list of strings
             we will sort your return value in output
    """
    def letter_case_permutation(self, s: str) -> List[str]:
        
        def _get_possible_char_lists(char: str) -> List[str]:
            if char.isalpha():
                if char.islower():
                    return [char, char.upper()]
                else:
                    return [char.lower(), char]
            else: #isdigit()
                return [char]

        def dfs(cur_idx: int, sublist: List[str]):
            nonlocal s, output_list
            if cur_idx == len(s):
                output_list.append("".join(sublist))
                return
            for char in _get_possible_char_lists(s[cur_idx]):
                sublist.append(char)
                dfs(cur_idx=cur_idx+1, sublist=sublist)
                sublist.pop()

        output_list = []
        if not s:
            output_list.append("")
            return output_list
        dfs(cur_idx=0, sublist=[])
        return output_list
```
#### Remark:
- [Subsets](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_17_Subsets.md#%E4%BA%8C%E5%8F%89%E6%A8%B9-1)的變形題
#### Submission:
```
163 ms
time cost
·
13.25 MB
memory cost
·
Your submission beats
8.80 %
Submissions
```
#### Complexity:
- Time: O(n * 2^n)
- Space: O(n)
