### Fruit Into Baskets
https://leetcode.com/problems/fruit-into-baskets/
>Given the integer array `fruits`, return the maximum number of fruits you can pick.
```python
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        dict_fruits = defaultdict(int)
        cur_max = 0
        while r < len(fruits):
            f = fruits[r]
            if f in dict_fruits: # seen fruit
                dict_fruits[f] += 1
            else: # new fruit
                while len(dict_fruits) > 1:
                    dict_fruits[fruits[l]] -= 1
                    if dict_fruits[fruits[l]] == 0:
                        del dict_fruits[fruits[l]]
                    l += 1
                dict_fruits[f] += 1
            r += 1
            cur_max = max(cur_max, r-l)
        return cur_max
```
#### Remark:
- When checking if key exists in `defaultdict`, do `if f in dict_fruits`. Don't access it, otherwise the key would be created.
#### Submission:
```
```
#### Complexity:
- Time: O(N)
- Space: O(2) = O(1)
