https://leetcode.com/problems/two-sum/
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
        """create a hash table in format of {'value': 'index'}
        """
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        return hashmap
```
#### Remark:
- 
#### Submission:
```
Runtime: 124 ms, faster than 45.61% of Python3 online submissions for Two Sum.
Memory Usage: 15.2 MB, less than 24.03% of Python3 online submissions for Two Sum.
```
#### Complexity:
- Time: O(n)
- Space: O(n)
