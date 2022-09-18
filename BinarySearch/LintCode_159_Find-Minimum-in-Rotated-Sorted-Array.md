### Find Minimum in Rotated Sorted Array
https://www.lintcode.com/problem/159/
>

```
OO...OXX....X
     ^^
  左上｜右下
    ↗ 
  ↗      
          ↗
        ↗
sorted array ∈ rotated sorted array
X的第一個數（右半部分的條件）：必須是<=整個數列最後一個數
```
```python
```
#### Remark:
- Followup: 如果有重複的數，可以證明，無法保證在log(n)的時間內解決
  - 例子[1, 1, 1, 1, ..., 1]裡面藏著一個0, 也是rotated sorted array 
    - 最壞情況是把所有traverse一次，O(n) 
#### Submission:
```
```
#### Complexity:
- Time:
- Space:
