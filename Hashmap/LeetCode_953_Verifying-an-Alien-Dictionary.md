### Verifying an Alien Dictionary
https://leetcode.com/problems/verifying-an-alien-dictionary/description/
>Given a sequence of `words` written in the alien language, and the `order` of the alphabet, return `true` if and only if the given words are sorted lexicographically in this alien language.
```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map_char2idx = {}
        for idx, char in enumerate(order):
            map_char2idx[char] = idx
        for i in range(len(words)-1):
            curr_word, next_word = words[i], words[i+1]
            for j in range(len(curr_word)):
                if j == len(next_word): # apple -> app
                    return False
                if curr_word[j] != next_word[j]:
                    if map_char2idx[curr_word[j]] > map_char2idx[next_word[j]]:
                        return False
                    else: # obeyed the rule
                        break # next word
        return True
```
#### Remark:
- 
#### Submission:
```
Runtime
31 ms
Beats
95.75%

Memory
14 MB
Beats
31.27%
```
#### Complexity:
- Time: O(len(words)*L) where L=len of max word
- Space: O(26)=O(1)
