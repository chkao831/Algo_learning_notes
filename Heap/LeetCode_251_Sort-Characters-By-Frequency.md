### Sort Characters By Frequency
https://leetcode.com/problems/sort-characters-by-frequency/
>Given a string `s`, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
>
>Return the sorted string. If there are multiple answers, return any of them.
```python
from heapq import heappop

class Solution:
    def frequencySort(self, s: str) -> str:
        # O(n)
        counter = Counter(s)
        heap = []
        # O(nlogn)
        for char in counter:
            heappush(heap, (-counter[char], char))
        # O(nlogn)
        str_out = ""
        while heap:
            (freq, c) = heappop(heap)
            for i in range(-freq):
                str_out += c
        return str_out
```
#### Remark:
- 使用maxHeap (freq加負號）
- 因為string is immutable, 可以在最後一步再把list轉str join起來 （時間複雜度不變）
  ```python
  list_out = []
      while heap:
          (freq, c) = heappop(heap)
          list_out.append(c*-freq)
      return "".join(list_out) # "".join(o for o in list_out)
  ```
- 甚至不需要用max heap去排，都用到counter了，可直接運用`counter.most_common()`（時間複雜度不變）
    - `most_common([n])`
        - 回傳一個 list，包含出現最多次的 `n` 個元素及其出現次數，並按照出現次數排序。如果 `n` 被省略或者為 `None`，`most_common()` 會回傳所有 `counter` 中的元素。**出現次數相同的元素會按照首次出現的時間先後來排列**：
            ```python
            Counter('abracadabra').most_common(3)
            >>> [('a', 5), ('b', 2), ('r', 2)]
            ```
 
  ```python
  def frequencySort(self, s: str) -> str:
      # O(n)
      counter = Counter(s)
      common = []
      # O(nlogn)
      for char, freq in counter.most_common():
          common.append(char*freq)
      return "".join(common)
  ```
  ```
  Runtime: 44 ms, faster than 94.03% of Python3 online submissions for Sort Characters By Frequency.
  Memory Usage: 15.2 MB, less than 98.50% of Python3 online submissions for Sort Characters By Frequency.
  ```
#### Submission:
```
Runtime: 55 ms, faster than 85.88% of Python3 online submissions for Sort Characters By Frequency.
Memory Usage: 15.2 MB, less than 81.15% of Python3 online submissions for Sort Characters By Frequency.
```
#### Complexity:
- Time: O(nlogn)
- Space: O(n)
