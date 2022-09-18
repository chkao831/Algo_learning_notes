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
```
#### Remark:
- 
#### Submission:
```
```
#### Complexity:
- Time:
- Space:
