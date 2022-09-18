方法一：先用[Lint159](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_159_Find-Minimum-in-Rotated-Sorted-Array.md)方法做一次二分，找到低谷，然後擇一方繼續二次二分

方法二：
```
             target
                v
OOO............OXX.......X
  ↗
 ↗
               ↗ 
             ↗
           ↗

如果target落在右下，X的條件為：t<=X1<last
如果target落在左上，X的條件為：X1>=t or X1<first
思路太複雜

於是 可以：
在一個rotated sorted array上切一刀，可以判斷出這一刀切在
rotation的左上半部分 還是右下半部分
劈出mid, mid>=start, 則在左上, otherwise(<start)則在右下，這兩個部分是沒有交集的
然後判斷target若是介於middle~end之間 往右邊去 反之往左邊去
這一刀的兩邊仍然是rotated sorted array
這樣的條件可以允許我們下一步繼續二分
```
