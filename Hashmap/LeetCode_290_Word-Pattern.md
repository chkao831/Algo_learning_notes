### Word Pattern
https://leetcode.com/problems/word-pattern/description/
>Given a `pattern` and a string `s`, find if `s` follows the same `pattern`.
>
>Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`.
```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict_char2word = {}
        dict_word2char = {}
        
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        
        for c, w in zip(pattern, words):
            if c not in dict_char2word:
                if w in dict_word2char:
                    return False
                else:
                    dict_char2word[c] = w
                    dict_word2char[w] = c
            else:
                if dict_char2word[c] != w:
                    return False
        return True
```
#### Remark:
- 為了避免`"abba" "dog dog dog dog"`返回True的情形，要做一個雙向的mapping
#### Submission:
```
Runtime
40 ms
Beats
63.75%

Memory
13.8 MB
Beats
74.33%
```
#### Complexity:
- Time: O(N)
- Space: O(U), where U = #unique words
