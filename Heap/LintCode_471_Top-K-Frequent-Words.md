### Top K Frequent Words
https://www.lintcode.com/problem/471/description
>Given a list of words and an integer `k`, return the top k frequent words in the list.\
>If two words has the same frequency, **the one with lower alphabetical order come first**.
```python
from typing import (
    List,
)
from collections import defaultdict
from heapq import heappush, heappop

class HeapItem:
    def __init__(self, count, word):
        self.count = count
        self.word = word
    
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word # 'abc' is bigger than 'xyz'
        return self.count < other.count

class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def top_k_frequent_words(self, words: List[str], k: int) -> List[str]:
        
        # Add counter, O(n)
        counter = defaultdict(int)
        for word in words:
            counter[word] += 1
        # For top k frequent, push to minHeap of size k. O(nlogk)
        heap = []
        for key, value in counter.items():
            heapItem = HeapItem(value, key) # trick, given same counts, refer to lexicon -> class HeapItem for new rule
            heappush(heap, heapItem)
            if len(heap) > k:
                heappop(heap)
        # With a minHeap of size k, pop items from small to big. O(klogk)
        out = []
        for _ in range(k):
            item = heappop(heap)
            out.append(item.word)
        # O(k) to reverse small->big to big->small
        out.reverse()
        return out
```
#### Remark:
- Trick:
  - 維持Top K(最大），用minHeap，只保留K，淘汰小的
  - 把次數小的淘汰掉，但當次數相同時，看字母順序（可規定的順序顛倒，必須是a>z），所以定義新的class的`__lt__`來達成 
#### Submission:
```
182 ms
time cost
·
8.52 MB
memory cost
·
Your submission beats
19.80 %
Submissions
```
#### Complexity:
- Time: O(nlogk)
- Space: O(n)
