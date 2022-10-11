### Letter Combinations of a Phone Number
https://www.lintcode.com/problem/425/
>Given a digit string excluded 0 and 1, return all possible letter combinations that the number could represent.
```python
from typing import (
    List,
)

DIGIT_TO_CHAR = {
    "2": "abc", 
    "3": "def",
    "4": "ghi",
    "5": "jkl", 
    "6": "mno", 
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

class Solution:
    """
    @param digits: A digital string
    @return: all possible letter combinations
             we will sort your return value in output
    """
    def letter_combinations(self, digits: str) -> List[str]:
        
        def dfs(startingIndex: int, sub: List[int]):
            if len(sub) == len(digits):
                results.append(''.join([s for s in sub])) # equiv. to ''.join(sub)
                return
            for char in DIGIT_TO_CHAR[digits[startingIndex]]:
                sub.append(char)
                dfs(startingIndex+1, sub)
                sub.pop()
        
        results = []
        if not digits:
            return results
        dfs(startingIndex=0, sub=[])
        return results
```
#### Remark:
- 如果有一個字典，要求組成的單詞都是字典裡的，優化方式？
    - [Lint 270 - Letter Combo II](https://www.lintcode.com/problem/270/solution/19786)     
        - 思路：這個題不需要 DFS，只需要建 Trie 就行。存在 Trie 里的不是單詞，而是單詞轉成數字之後的字符串。比如詞典里有 `["a", "abc", "de", "fg"]`，存在 Trie 里的就是 `["2", "222", "33", "34"]` 之後的話 for queries 里的每個 query，在 Trie 里沿著 query 走到對應的節點上看一下計數就行。
#### Submission:
```
82 ms
time cost
·
6.06 MB
memory cost
·
Your submission beats
38.40 %
Submissions
```
#### Complexity:
- Time: O(4^len(digits) * len(digits)) in the worst case (總方案數*構建方案所需時間) 
- Space: O(len(digits))
