### Decode Ways
https://leetcode.com/problems/decode-ways/
>Given a string s containing only digits, **return the number of ways** to decode it.
```python
class Solution:
    def numDecodings(self, s: str) -> int:

        @lru_cache(None)
        def dfs(s):
            if not s: return 1 # when we reached the end, s[len(s):] returns an empty string
            if s[0]=='0': return 0

            # see whether first two chars comprise a legitimate integer n such that 1 <= n <= 26.
            # if legitimate, slice its chars from the string and recurse the remaining string
            if len(s) > 1 and int(s[:2]) < 27: 
                
                return dfs(s[1:]) + dfs(s[2:]) # if s[2] yields index out of bound, s[2:] would simply return ""

            return dfs(s[1:])      
        
        return dfs(s)
```
#### Remark:
```
# Here's the plan:
  #    Use dp such that at each call, we decide whether the first one char
  #    or the first two chars each comprise a legitimate integer n such that
  #    1 <= n <= 26. For each legitimate integer, we slice its chars from the string 
  #    and recurse the remaining string. For each illegitimate integer, we stop. We 
  #    count the leaves that each exhaust the string of digits
  #    
  #    For example, let s = 1202421. The tree shows the application of this recursion:

  #                          __________________root_______________________
  #                         /                                              \
  #               _________1_______                               __________12_________
  #              /                 \                             /                     \
  #         ____2___             ___20_____                     0                      02 
  #        /        \           /           \                   X                       X
  #       0          02        2 ____        24              
  #       X           X       /      \       / \           
  #                          4       42    2    21 
  #                         /  \      X   /      *
  #                        2   21        1
  #                       /     *        *
  #                      1
  #                      *
  #  The legitimate and illegitimate strings are labeled * and X respectively.
  #  The legitimate strings: 1,20,2,4,2,1 --> atdbba 
  #                          1,20,2,4,21  --> atdbu
  #                          1,20,24,2,1  --> atxba
  #                          1,20,24,21   --> atxu
  #  The answer is 4.
```
#### Submission:
```
Runtime: 48 ms, faster than 72.51% of Python3 online submissions for Decode Ways.
Memory Usage: 14.3 MB, less than 11.91% of Python3 online submissions for Decode Ways.
```
#### Complexity:
- Time: O(2^digits)
- Space: O(h^2) (recursion depth=h; at each iteration, generate (slice) new string of length h)
