### Alien Dictionary
https://www.lintcode.com/problem/892/description
>
```python
from typing import (
    List,
)
from collections import defaultdict
from heapq import heapify, heappop, heappush

class Solution:
    
    def __init__(self):
        self.dict_char_order = defaultdict(set)
        self.dict_indeg = defaultdict(int)

    def alien_order(self, words: List[str]) -> str:
        """
        @param words: a list of words
        @return: a string which is correct order
        """

        def build_dict_char() -> bool:
            num_words = len(words)
            for word_idx in range(num_words-1):
                last_pos = min(len(words[word_idx]), len(words[word_idx+1]))
                for char_idx in range(last_pos):
                    if words[word_idx][char_idx] != words[word_idx+1][char_idx]: # car/cat
                        former, latter = words[word_idx][char_idx], words[word_idx+1][char_idx] # r/t
                        self.dict_char_order[former].add(latter)
                        break
                    if char_idx == last_pos - 1: # windy/wind
                        if len(words[word_idx]) > len(words[word_idx+1]):
                            return False
            return True

        def build_dict_indeg():
            for word in words:
                for char in word:
                    self.dict_indeg[char] = 0
            for pre, posts in self.dict_char_order.items():
                for post in posts:
                    self.dict_indeg[post] += 1

        dict_char = build_dict_char()
        if not dict_char:
            return ""
        build_dict_indeg()
        queue = [c for c in self.dict_indeg if self.dict_indeg[c]==0]
        heapify(queue) # to return the smallest in normal lexicographical order
        str_out = ""
        while queue:
            char = heappop(queue)
            str_out += char
            for next_char in self.dict_char_order[char]:
                self.dict_indeg[next_char] -= 1
                if self.dict_indeg[next_char] == 0:
                    heappush(queue, next_char)
        return str_out if len(str_out)==len(self.dict_indeg) else ""
```
#### Remark:
- Forgot to break
#### Submission:
```
81 ms
time cost
·
5.92 MB
memory cost
·
Your submission beats
99.00 %
Submissions
```
#### Complexity:
- Time: 
- Space: 
