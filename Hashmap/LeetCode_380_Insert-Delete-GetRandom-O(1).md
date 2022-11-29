### Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/
>Implement the `RandomizedSet` class:
>
>`RandomizedSet()` Initializes the RandomizedSet object.\
>`bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.\
>`bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.\
>`int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.\
>You must implement the functions of the class such that each function works in average O(1) time complexity.

<p>
    <img src="https://leetcode.com/problems/insert-delete-getrandom-o1/Figures/380/delete.png" width="600" />
</p>

```python
class RandomizedSet:

    def __init__(self):
        self.list_nums = []
        self.dict_numToIdx = {}

    def insert(self, val: int) -> bool:
        if val in self.list_nums:
            return False
        else:
            self.list_nums.append(val)
            self.dict_numToIdx[val] = len(self.list_nums)-1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.list_nums:
            return False
        else:
            old_idx, new_val = self.dict_numToIdx[val], self.list_nums[-1]
            self.dict_numToIdx[new_val] = old_idx
            self.list_nums[old_idx] = new_val
            # clear up
            del self.dict_numToIdx[val]
            self.list_nums.pop()
            return True
        
    def getRandom(self) -> int:
        idx = random.randint(0, len(self.list_nums)-1)
        return self.list_nums[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```
#### Remark:
- Key: 近似於堆(Heap)的操作
  - 當一個特定位置的元素被刪除時，最末位的元素成為該位置的replacement
  - 記得要pop掉數組最末位＋del掉哈希表索引 
#### Submission:
```
Runtime: 2597 ms, faster than 5.02% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 61.3 MB, less than 74.27% of Python3 online submissions for Insert Delete GetRandom O(1).
```
#### Complexity:
- Time:  GetRandom is always O(1). Insert and Delete both have O(1) average time complexity, and O(N) in the worst-case scenario when the operation exceeds the capacity of currently allocated array/hashmap and invokes space reallocation.
- Space: O(N) to store N elements.
