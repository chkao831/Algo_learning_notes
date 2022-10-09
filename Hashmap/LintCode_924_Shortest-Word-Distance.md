### Shortest Word Distance
https://www.lintcode.com/problem/924/description
>Given a list of `words` and two words `word1` and `word2`, return the shortest distance between these two words in the list.\
>You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
```python
from typing import (
    List,
)
from collections import defaultdict

class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    
    def shortest_distance(self, words: List[str], word1: str, word2: str) -> int:
        hashmap = defaultdict(list)
        for idx, word in enumerate(words):
            if word1 == word or word2 == word:
                hashmap[word].append(idx)
        min_val = float("inf")
        if len(hashmap[word1])>0 and len(hashmap[word2])>0:
            for i in hashmap[word1]:
                for j in hashmap[word2]:
                    min_val = min(min_val, abs(i-j))
            return min_val
        return -1

```
#### Remark:
- 
#### Submission:
```
81 ms
time cost
·
8.00 MB
memory cost
·
Your submission beats
99.60 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(n)
