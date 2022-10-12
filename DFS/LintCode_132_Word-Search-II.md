### Word Search II
https://www.lintcode.com/problem/132/
> Given a matrix of lower alphabets and a dictionary. Find all **unique** words in the dictionary that can be found in the matrix. 

<p>
    <img src="https://assets.leetcode.com/uploads/2020/11/07/search1.jpg" width="300" />
</p>

```python
from typing import (
    List, Dict
)

DIRECTIONS = {
    (0, 1), (1, 0), (0, -1), (-1, 0)
}

class Solution:

    def word_search_i_i(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        @param board: A list of lists of character
        @param words: A list of string
        @return: A list of string
                 we will sort your return value in output
        """

        def get_visited_board() -> List[List[bool]]:
            visited_board = [[False for j in range(len(board[0]))] for i in range(len(board))]
            return visited_board

        def get_prefix_to_bool() -> Dict:
            out = {}
            for word in words:
                for idx in range(len(word)):
                    pre = word[:idx+1]
                    if pre not in out:
                        out[pre] = False
                out[word] = True
            return out

        def is_valid(x: int, y: int) -> bool:
            if 0<=x<len(board) and 0<=y<len(board[0]):
                return True
            return False

        def dfs(visited: List[List[bool]], x: int, y: int, subword: str):
            
            if subword not in dict_prefix_to_bool:
                return
            if dict_prefix_to_bool[subword] == True:
                results.add(subword) # 不能return!
                
            for d in DIRECTIONS: # recursive
                if not is_valid(x+d[0], y+d[1]) or visited[x+d[0]][y+d[1]]:
                    continue
                visited[x+d[0]][y+d[1]] = True
                dfs(visited, x+d[0], y+d[1], subword+board[x+d[0]][y+d[1]])
                visited[x+d[0]][y+d[1]] = False

        results = set()
        visited_board = get_visited_board()
        dict_prefix_to_bool = get_prefix_to_bool()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not is_valid(i,j):
                    continue
                visited_board[i][j] = True
                dfs(visited_board, i, j, board[i][j])
                visited_board[i][j] = False
        return list(results)
```
#### Remark:
- `if dict_prefix_to_bool[subword] == True:` **不能當作**ending **base**, 只能當作成功了，但可能接著還有機會連下去，不能直接return。
- 建立predix dictionary時，本來使用`defaultdict`，想免掉`if pre not in out`的判斷
  - 但這樣反而可能蓋掉原本value已經被弄成`True`的key，如
    ```
    [['b'], ['a'], ['b'], ['b'], ['a']]
    {'b': True, 'ba': True, 'bab': False, 'babb': False, 'babba': False, 'babbab': True, 'a': True}
    ```
    用`defaultdict`直接蓋，`'b'`就會在`'ba'`的loop裡變成`False`，所以還是用一般dictionary, 沒有再加。
#### Submission:
```
773 ms
time cost
·
6.55 MB
memory cost
·
Your submission beats
29.80 %
Submissions
```
#### Complexity:
- Time: O(m*n*4^(longest_len_of_word))
- Space: O(m*n) (for `visited_board`) (also, the recursion depth is the longest possible length of word(or prefix), and do note that we create new string at every recursive call)
