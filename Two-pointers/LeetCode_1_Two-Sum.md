[https://leetcode.com/problems/two-sum/

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        @return: indices of the two numbers that add up to target, in any order
        """
        indexed_pair = self.getPair(nums)
        sorted_pair = sorted(indexed_pair, key=lambda indexed_pair: indexed_pair[1]) # sorted by value, O(nlogn)

        left, right = 0, len(nums)-1
        while left < right:
            if sorted_pair[left][1] + sorted_pair[right][1] == target:
                return [sorted_pair[left][0], sorted_pair[right][0]] # in any order
            elif sorted_pair[left][1] + sorted_pair[right][1] < target:
                left += 1
            else:
                right -= 1
        return []
    
    def getPair(self, nums: List[int]) -> Tuple:
        """
        @return: a list consisting of tuple pairs (index, value)
        """
        indices = list(range(0, len(nums)))
        pair = list(zip(indices, nums))
        return pair
```
#### Remark:
- Need to return indices (of unsorted numbers) in any order, so need a supporting method to record this
- if indices should be returned in ascending order, the return argument would instead become `return [min(sorted_pair[left][0], sorted_pair[right][0]), max(sorted_pair[left][0], sorted_pair[right][0])]`
#### Submission:
```
Runtime: 112 ms, faster than 53.77% of Python3 online submissions for Two Sum.
Memory Usage: 15.4 MB, less than 13.72% of Python3 online submissions for Two Sum.
```
#### Complexity:
- Time: O(nlogn)
- Space: O(n)
](https://leetcode.com/problems/two-sum/

## Hashmap

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
- For the one-pass approach, I originally misplaced the addition line `hashmap[nums[i]] = i` immediately after entering the for loop. It doesn't work because of the nature of hashmap, such an arrangement overwrites the value corresponding to a key when we're looking for its complement. Hence, as an example, we wouldn't find a solution in such a case: `[3, 3], target = 6`. 
#### Submission:
```
Runtime: 124 ms, faster than 45.61% of Python3 online submissions for Two Sum.
Memory Usage: 15.2 MB, less than 24.03% of Python3 online submissions for Two Sum.
```
```
Runtime: 121 ms, faster than 47.40% of Python3 online submissions for Two Sum.
Memory Usage: 15.1 MB, less than 63.71% of Python3 online submissions for Two Sum.
```
#### Complexity:
- Time: O(n)
- Space: O(n)

## Two pointers
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        @return: indices of the two numbers that add up to target, in any order
        """
        indexed_pair = self.getPair(nums)
        sorted_pair = sorted(indexed_pair, key=lambda indexed_pair: indexed_pair[1]) # sorted by value, O(nlogn)

        left, right = 0, len(nums)-1
        while left < right:
            if sorted_pair[left][1] + sorted_pair[right][1] == target:
                return [sorted_pair[left][0], sorted_pair[right][0]] # in any order
            elif sorted_pair[left][1] + sorted_pair[right][1] < target:
                left += 1
            else:
                right -= 1
        return []
    
    def getPair(self, nums: List[int]) -> Tuple:
        """
        @return: a list consisting of tuple pairs (index, value)
        """
        indices = list(range(0, len(nums)))
        pair = list(zip(indices, nums))
        return pair
```
#### Remark:
- Need to return indices (of unsorted numbers) in any order, so need a supporting method to record this
- if indices should be returned in ascending order, the return argument would instead become `return [min(sorted_pair[left][0], sorted_pair[right][0]), max(sorted_pair[left][0], sorted_pair[right][0])]`
#### Submission:
```
Runtime: 112 ms, faster than 53.77% of Python3 online submissions for Two Sum.
Memory Usage: 15.4 MB, less than 13.72% of Python3 online submissions for Two Sum.
```
#### Complexity:
- Time: O(nlogn)
- Space: O(n)
)
