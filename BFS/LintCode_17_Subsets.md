## Subsets
https://www.lintcode.com/problem/17/

<img src="../images/17_Subsets.png" />

>Given a set with distinct integers, return all possible subsets.

### N叉樹
- 取queue元素時，沒有真的pop掉頭
  - 只是用一個int去算count
- `while queue` 同理 也是判斷 當前要取的元素還夠取（相當於隊列不空）
- `if`語句：當目前的`subset`存在、並且最後一個數字比即將進來的大的話，不加（為了去重）
- `queue.append(subset + [num])` 是沒有修改到`subset`本身的
   
```python
from typing import (
    List,
)

class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        @param nums: A set of numbers
        @return: A list of lists
                we will sort your return value in output
        """
        
        if not nums:
            return [[]]
        queue = [[]] # len = 0
        q_index_count = 0
        while q_index_count < len(queue):
            subset = queue[q_index_count] # [] -> [1] -> [2] -> [3] -> [1, 2] -> [1, 3] -> [2, 3] -> [1, 2, 3]
            q_index_count += 1
            for num in nums:
                if subset and subset[-1] >= num:
                    continue
                queue.append(subset + [num])
        return queue
```
#### Submission:
```
102 ms
time cost
·
6.07 MB
memory cost
·
Your submission beats
33.20 %
Submissions
```
#### Complexity:
- Time: O(2^n)
- Space: O(2^n)

### 二叉樹
- `sorted(nums)`相當於n叉樹做法中的`if`語句，為了去重
- `subset`是會被修改的(in-place append)
```python
from typing import (
    List,
)

class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        @param nums: A set of numbers
        @return: A list of lists
                we will sort your return value in output
        """
        
        if not nums:
            return [[]]
        queue = [[]] # len = 0
        for num in sorted(nums):
            for i in range(len(queue)):
                subset = list(queue[i])
                subset.append(num)
                queue.append(subset)
                print("num is {} and queue is {}".format(num, queue))
        return queue
```
- std out
  - input: [1,2,3] 
  ```
  num is 1 and queue is [[], [1]]
  num is 2 and queue is [[], [1], [2]]
  num is 2 and queue is [[], [1], [2], [1, 2]]
  num is 3 and queue is [[], [1], [2], [1, 2], [3]]
  num is 3 and queue is [[], [1], [2], [1, 2], [3], [1, 3]]
  num is 3 and queue is [[], [1], [2], [1, 2], [3], [1, 3], [2, 3]]
  num is 3 and queue is [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
  ```
#### Submission:
```
101 ms
time cost
·
6.19 MB
memory cost
·
Your submission beats
63.40 %
Submissions
```
#### Complexity:
- Time: O(2^n * 2 - 1)
- Space: O(2^n)
