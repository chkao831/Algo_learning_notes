 #### 倍增法 (Exponential Backoff，指數回退)
 ```
 [ 0, 1, 2, 3, ..., k, ...]
                    ^
                  target
```
To find the target in log(k) time, try Exponential Backoff.\
Similar scenarios that apply Exponential Backoff: ArrayList in Java, vector in C++, 網路重試, etc.\
Worst Scenario: **O(log(2k-2)) = O(log(k))**
```
1 -> 2 -> 4 -> 8 -> ... -> k-1 -> 2k-2
 [ 0, 1, 2, 3, ...k-1, k, ...]
                   ^
                 stop here
                 then next time to
 [ 0, 1, 2, 3, ...k-1, k, ..., 2k-2]                
```
#### Remark:
- kth number, has index of (k - 1)
  - use kth number to multiply by 2
