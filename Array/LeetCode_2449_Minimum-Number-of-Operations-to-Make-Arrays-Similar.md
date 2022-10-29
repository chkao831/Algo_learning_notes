### Minimum Number of Operations to Make Arrays Similar
https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

```python
class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        target.sort()
        source_odd, source_even = [num for num in nums if num%2==1], [num for num in nums if num%2==0]
        target_odd, target_even = [num for num in target if num%2==1], [num for num in target if num%2==0]
        val = 0
        for idx,_ in enumerate(target_odd):
            val += max(0, target_odd[idx]-source_odd[idx])
        for idx,_ in enumerate(target_even):
            val += max(0, target_even[idx]-source_even[idx])
        return val // 2
```
#### Remark:
- Split to even & odd cases; discuss separately
- 因為題幹保證了The test cases are generated such that `nums` can always be similar to `target`, 所以只要管source->target要補多少（只要看正的值），source->target要被補多少（負的值）不用管，因為一定補得剛剛好
#### Submission:
```
Runtime: 2596 ms, faster than 27.09% of Python3 online submissions for Minimum Number of Operations to Make Arrays Similar.
Memory Usage: 32.6 MB, less than 69.79% of Python3 online submissions for Minimum Number of Operations to Make Arrays Similar.
```
#### Complexity:
- Time: O(n)
- Space: O(n)
