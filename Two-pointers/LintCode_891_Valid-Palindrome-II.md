https://www.lintcode.com/problem/891/

```python
class Solution:
    """
    @param s: an non-empty string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def valid_palindrome(self, s: str) -> bool:
        """main function
        """
        left_start, right_start = 0, len(s)-1
        # retrieve first illegal position
        left_post, right_post = self.find_position(s, left_start, right_start)
        if (left_post >= right_post): return True # no illegal char

        # check remaining part
        return self.remaining_palindrome(s, left_post+1, right_post) or \
        self.remaining_palindrome(s, left_post, right_post-1)

    def find_position(self, s:str, l:int, r:int) -> tuple:
        """given a string and starting left and right position, return pointers'
        tuple of illegal position (if illegal) or until two pointers meet.

        @return: tuple of two integers
        """
        while l < r:
            # no need to also check if l < r, because pointers don't move before
            # this if judgment at this round of loop
            if s[l] != s[r]:
                return l, r
            l += 1
            r -= 1
        return l, r
    
    def remaining_palindrome(self, s:str, l: str, r:int) -> bool:
        """given a string and starting left and right position, check if
        the designated part consists of a valid palindrome.
        """
        final_left, final_right = self.find_position(s, l, r)
        return final_left >= final_right
```
#### Submission:
```
101 ms
time cost
·
5.98 MB
memory cost
·
Your submission beats
58.60 %
Submissions
```
#### Remark:
- hesitant about function splitting design, inputs and returns
#### Complexity
- Time: O(n)
- Space: No extra memory
