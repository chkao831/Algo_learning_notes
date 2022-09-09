https://leetcode.com/problems/two-sum/

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
