### Permutation Index

https://www.lintcode.com/problem/197/
> Given a permutation which contains no repeated number, find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.\
> 題目：給出一個不含重複數字的排列，求這些數字的所有排列按字典序排序後該排列的編號，編號從1開始。例如排列 [1, 2, 4] 是第 1 個排列。
```python
from typing import (
    List,
)

class Solution:

    def permutationIndex(self, A):
        """
        @param A: An array of integers
        @return: A long integer
        """
        
        permutation = 1
        result = 0
        for i in range(len(A) - 2, -1, -1):
            smaller = 0
            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    smaller += 1
            result += smaller * permutation
            permutation *= len(A) - i
        return result + 1
```
#### Remark:
- 只需計算有多少個排列在當前排列A的前面即可。如何算呢?舉個例子，`[3,7,4,9,1]`，在它前面的必然是某位置i對應元素比原數組小，而i左側和原數組一樣。也即 `[3,7,4,1,X] ， [3,7,1,X,X] ， [3,1或4,X,X,X] ， [1,X,X,X,X]` 。
- 而第`i`個元素，比原數組小的情況有多少種，其實就是`A[i]`右側有多少元素比`A[i]`小，乘上`A[i]`右側元素全排列數，即`A[i]`右側元素數量的階乘。`i`從右往左看，比當前`A[i]`小的右側元素數量分別為`1,1,2,1`，所以最終字典序在當前`A`之前的數量為`1×1!+1×2!+2×3!+1×4!=39`，故當前`A`的字典序為 40。
- 具體步驟：
  - 用`permutation`表示當前階乘，初始化為 1, `result` 表示最終結果，初始化為 0 。由於最終結果可能巨大，所以用 long 類型。 
  - i從右往左遍歷`A`，循環中計算`A[i]`右側有多少元素比`A[i]`小，計為 smaller ， `result += smaller * permutation` 。之後 `permutation *= A.length - i` ，為下次循環 i 左移一位後的排列數。
  - 已算出多少字典序在`A`之前，返回`result + 1`。
- Q: 元素有重復怎麼辦？
  - A: 好問題！元素有重復，情況會複雜的多。因為這會影響 A[i] 右側元素的排列數，此時的排列數計算方法為總元素數的階乘，除以各元素值個數的階乘，例如 [1, 1, 1, 2, 2, 3] ，排列數為6! ÷ (3! × 2! × 1!) 。為了正確計算階乘數，需要用哈系表記錄 A[i] 及右側的元素值個數，並考慮到 A[i] 與右側比其小的元素 A[k] 交換後，要把 A[k] 的計數減一。用該哈系表計算正確的階乘數。而且要注意，右側比 A[i]小 的重復元素值只能計算一次，不要重復計算！

#### Submission:
```
122 ms
time cost
·
7.60 MB
memory cost
·
Your submission beats
6.80 %
Submissions
```
#### Complexity:
- Time: O(n^2)
- Space: O(1)
