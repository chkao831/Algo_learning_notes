# Intersection of Arrays
https://www.lintcode.com/problem/793/
>

## 1. Hashmap
```python

class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        count = {}
        # 记录每个数的出现次数
        for arr in arrs:
            for x in arr:
                if x not in count:
                    count[x] = 0
                count[x] += 1
        
        # 某个数出现次数等于数组个数，代表它在所有数组中都出现过
        result = 0
        for x in count.keys():
            if count[x] == len(arrs):
                result += 1
        return result
```
#### Remark:
- 由于题目数据中每个数组里的元素都没有__重复__，而这道题目又要求求交集，交集中的元素一定在每一个数组中都出现过，所以交集中的元素在所有数组中的出现次数一定等于数组个数。所以使用Map或Python中的字典数据结构就可以统计数字出现的次数，就可以解决问题了。


#### Submission:
```
```
#### Complexity:
- Time: O(nk)
- Space: O(k)

## 2. Hashmap (-)
```python
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        numShouldBe = len(arrs) - 1
        remains = {}

        for n in arrs[0]:
            remains[n] = numShouldBe

        ans = 0
        for i in range(1, len(arrs)):
            for n in arrs[i]:
                if n not in remains:
                    continue

                remains[n] -= 1
                if remains[n] == 0:
                    del remains[n]
                    ans += 1

                if len(remains) == 0:
                    return ans

        return ans
```
#### Remark:
- 選一列作為 dict (優化：選最短列)，賦予剩下應出現的次數。
搜尋其他列，當 dict 數字減至零，代表找到一答案。


#### Submission:
```
```
#### Complexity:
- Time: O(nk)
- Space: O(k)

## 3. Heap
```python
import heapq
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        p_queue = []
        for i, arr in enumerate(arrs):
            if len(arr) == 0:
                return 0
            arr.sort()
            heapq.heappush(p_queue, (arr[0], (i, 0)))
            
        last_value, count, intersection = 0, 0, 0
        while p_queue:
            val, ind_tuple = heapq.heappop(p_queue)
            if count == 0 or val != last_value:
                if count == len(arrs):
                    intersection += 1
                last_value = val
                count = 1
            else:
                count += 1
                
            new_ind_tuple = (ind_tuple[0], ind_tuple[1] + 1)
            if new_ind_tuple[1] < len(arrs[new_ind_tuple[0]]):
                val = arrs[new_ind_tuple[0]][new_ind_tuple[1]]
                heapq.heappush(p_queue, (val, new_ind_tuple))
                
        if count == len(arrs):
            intersection += 1
        return intersection
```
#### Remark:
- 
#### Submission:
```
```
#### Complexity:
- Time: O(nklogk + knlogn)
- Space: O(nk)
