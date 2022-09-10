https://leetcode.com/problems/two-sum/

**Only one valid answer exists** and **can return the answer in any order**.  

```python
class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = self.createMap(nums) # O(n) time + O(n) space
        for i in range(len(nums)): # O(n) time
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i: # complement exists and is not itself
                return [i, hashmap[complement]]
        return []
    
    def createMap(self, nums):
        """create a hash table in format of {value: index}
        """
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        return hashmap
```
Can also do it in one-pass.
```python
class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i: # complement exists and is not itself
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
```
#### Remark:
- For the one-pass approach, I originally misplaced the addition line `hashmap[nums[i]] = i` immediately after entering the for loop. It doesn't work because of the nature of hashmap, this overwrites the value corresponding to a key when we're looking for its complement. Hence, as an example, we wouldn't find a solution in such a case: `[3, 3], target = 6`. 
#### Submission:
```
Runtime: 124 ms, faster than 45.61% of Python3 online submissions for Two Sum.
Memory Usage: 15.2 MB, less than 24.03% of Python3 online submissions for Two Sum.
```
```

```
#### Complexity:
- Time: O(n)
- Space: O(n)
