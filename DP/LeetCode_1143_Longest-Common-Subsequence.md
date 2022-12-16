### Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/description/
>Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return 0.

```python
from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            
            # Base case: If either string is now empty, we can't match
            # up anymore characters.
            if p1 == len(text1) or p2 == len(text2):
                return 0
            
            # Option 1: We don't include text1[p1] in the solution.
            option_1 = memo_solve(p1 + 1, p2)
            
            # Option 2: We include text1[p1] in the solution, as long as
            # a match for it in text2 at or after p2 exists.
            first_occurence = text2.find(text1[p1], p2)
            option_2 = 0
            if first_occurence != -1:
                option_2 = 1 + memo_solve(p1 + 1, first_occurence + 1)
            
            # Return the best option.
            return max(option_1, option_2)
                
        return memo_solve(0, 0)
```
#### Remark:
- Memoization
  - If the line is part of solution
    <p>
    <img src="https://leetcode.com/problems/longest-common-subsequence/solutions/598321/Figures/1143/subproblem_1.png" width="500" />
    </p>

  - If the line is not part of solution
    <p>
    <img src="https://leetcode.com/problems/longest-common-subsequence/solutions/598321/Figures/1143/subproblem_2.png" width="500" />
    </p>
    
#### Submission:
```
Runtime
1058 ms
Beats
56.94%

Memory
143.9 MB
Beats
6.11%
```
#### Complexity:
- Time: O(MN^2)
  - The input parameters to the recursive function are a pair of integers; representing a position in each string. There are M possible positions for the first string, and N for the second string. Therefore, this gives us MN possible pairs of integers, and is the number of subproblems to be solved.
  - Solving each subproblem requires, in the worst case, an O(N) operation; searching for a character in a string of length N. This gives us a total of O(M*N^2)
- Space: O(MN)
  - A total of MN subproblems to solve. 
