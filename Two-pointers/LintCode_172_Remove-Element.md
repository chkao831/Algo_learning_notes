### Remove Element
https://www.lintcode.com/problem/172/description
>給定一個數組 `A` 和一個值 `elem`，在邏輯上刪除與值 `elem` 相同的數字，返回新數組的長度 `n`，使得數組的前 `n` 個元素中，包含原數組 `A` 中所有不等於 `elem` 的數字。
>
>你需要修改數組 `A` 中的元素順序，並返回數組 `A` 中所有不等於 `elem` 的數字個數。\
>**需要在原數組中操作**\
>**修改後的數組前 n 個元素不需要有序**
```python
class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        left, right = 0, len(A)-1
        while left <= right:
            if A[left] == elem:
                A[left], A[right] = A[right], A[left]
                right -= 1
            else:
                left += 1
        return left
```
#### Remark:
- 為了在原數組上操作，使用雙指針達成。
#### Submission:
```
1208 ms
time cost
·
6.10 MB
memory cost
·
Your submission beats
18.20 %
Submissions
```
#### Complexity:
- Time: O(n)
- Space: O(1)
