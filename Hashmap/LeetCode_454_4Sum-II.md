An extension of [Lint607](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LintCode_607_Two-Sum-III-Data-structure-design.md)
```python
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        hashmap = {}
        for num1 in nums1:
            for num2 in nums2:
                hashmap[num1+num2] = hashmap.get(num1+num2, 0) + 1
        for num3 in nums3:
            for num4 in nums4:
                # want num1+num2+num3+num4 = 0 => num1+num2=-(num3+num4)
                count += hashmap.get(-(num3+num4), 0)
        return count
```
#### Remark:
- made a typo: `hashmap[num1+num2] = hashmap.get(num1+num2, 0) + 1`, not `hashmap.get(num1+num2) = hashmap.get(num1+num2, 0) + 1`
- if cares about **number of policies** (like this), then can partition and achieve **O(n^2)** time; \
  if cares about **policy content**, then could only achieve at **O(n^4)** at best
#### Submission:
```
Runtime: 1447 ms, faster than 23.96% of Python3 online submissions for 4Sum II.
Memory Usage: 14.1 MB, less than 70.11% of Python3 online submissions for 4Sum II.
```
#### Complexity:
- Time: O(n^2)
- Space: O(n^2) for hashmap
