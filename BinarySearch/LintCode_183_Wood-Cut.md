### Wood Cut
https://www.lintcode.com/problem/183/
> Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.\
>The unit of length is centimeter. The length of the woods are all positive integers, **you couldn't cut wood into float length. If you couldn't get >= k pieces, return 0.**
```
step1: 確定答案範圍 -> step 2: 驗證答案大小
step1: 小木頭的長度不可能比最長原木更長; 小木頭的長度不可能比所有原木總合除以k更長

  可以二分的原因：
  如果能切出k段長度為length的小木頭，一定能切出k段比length更短的木頭。
  如果不能切出k段長度為length的小木頭，一定不能切出k段比length更長的木頭。

step2:
L=[232, 124, 456]
length =  1   2   3 ... 113 114 115
k      = 812 406 270 ... 7   7   6 
把232, 124, 456拎出來，單獨除以想要的length，個數加起來，看有沒有>=k，是就O，反之則X

基於答案取值範圍有OOXX, 不是數組 
length = 1 2 3 4 5 6 7 ...
         O O O O X X X ...
凡滿足n, 必滿足n-1 and so on
找last position that satisfies
```

```python
from typing import (
    List,
)

class Solution:
    """
    @param l: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def wood_cut(self, l: List[int], k: int) -> int:

        def get_pieces(length: int) -> int: # O(n)
            return (sum(each_l//length for each_l in l))

        if not l or k<1:
            return 0
        max_len = min(max(l), sum(l)//k)
        start, end = 1, max_len
        if start > end:
            return 0

        while start + 1 < end:
            mid = (start+end)//2
            if get_pieces(mid) >= k:
                start = mid
            else: # get_pieces(mid) < k
                end = mid
        if get_pieces(end)>=k: return end
        if get_pieces(start)>=k: return start
        return 0
```
#### Remark:
- start (left pointer) 初始值=1, 因為長度不能為0
- 最後check時，先check後(`if get_pieces(end)>k`), 因為要找**last position that satisfies**
- 忘記加edge case: `if start > end: return 0`
#### Submission:
```
165 ms
time cost
·
7.19 MB
memory cost
·
Your submission beats
30.00 %
Submissions
```
#### Complexity:
- Time: O(nlogn)
- Space: O(1)
