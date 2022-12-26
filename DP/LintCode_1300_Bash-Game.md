## Bash Game
https://www.lintcode.com/problem/1300/description
>You are playing the following game with your friend: There is a pile of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove stones.

### 記憶化搜索
```python
from functools import lru_cache

class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    def can_win_bash(self, n: int) -> bool:
        
        @lru_cache(None)
        def dfs(stones: int) -> bool:
            if stones <= 3:
                return True
            for feasible_stones in range(1, 4):
                if dfs(stones-feasible_stones) is False:
                    return True
            return False

        return dfs(stones=n)
```
#### Submission:
```
TLE
```
#### Complexity:
如果時間複雜度和遞歸深度都是O(N)級別時容易StackOverflow
- Time: O(N)
- Space: O(N)

### Math
讓我們考慮一些小例子。顯而易見的是，如果石頭堆中只有一塊、兩塊、或是三塊石頭，那麼在你的回合，你就可以把全部石子拿走，從而在遊戲中取勝；如果堆中恰好有四塊石頭，你就會失敗。因為在這種情況下不管你取走多少石頭，總會為你的對手留下幾塊，他可以將剩餘的石頭全部取完，從而他可以在遊戲中打敗你。因此，要想獲勝，在你的回合中，必須避免石頭堆中的石子數為4的情況。
```python
class Solution:
    def canWinBash(self, n: int) -> bool:
        return n % 4 != 0
```
#### Submission:
```
101 ms
time cost
·
5.93 MB
memory cost
·
Your submission beats
30.00 %
Submissions
```
#### Complexity:
- Time: O(1)
- Space: O(1)
