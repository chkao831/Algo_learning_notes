### Copy Books
https://www.lintcode.com/problem/437/
> Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.
>
>These books list in a row and each person can claim a continous range of books. For example, one copier can copy the books from i-th to j-th continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).
>
>They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?
>
>Return the shortest time that the slowest copier spends.

```
step1: 確定答案範圍 -> step 2: 驗證答案大小

step1:
所求為時間，最少要花費幾個時間單位。
例如要抄的書有三本，分別是[3, 2, 4]
最少的時間單位不可能比4更少，最多的時間單位不可能比3+2+4多（全部都一個人抄）。
由此得出start, end = max(pages), sum(pages)
  
  可以二分的原因：
  如果k人能在limit_time抄完，那麼k人一定能在limit_time+1抄完。
  如果k人不能在limit_time抄完，那麼k人一定不能在limit_time-抄完。
  
step 2:
時間 和 抄書人數 之間有負相關映射關係

基於答案取值範圍有OOXX
pages=[...]
time = 1, 2, 3, 4, 5...(所求)
       X  X  X  O  O   (find first position of target)
copiers = 多.......少...
看copiers有沒有在k人以內，有，則人夠，還可以更少人。沒有則人不夠，還要再加人。
```

```python
```
#### Remark:
- 和[Lint183 - Wood_Cut](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_183_Wood-Cut.md)搭配服用

#### Submission:
```
```
#### Complexity:
- Time: O(nlog(sum-max))
- Space: O(1)
