### Minimum Number of Arrows to Burst Balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

<p>
    <img src="https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/solutions/288049/Figures/452/sorted.png" width="500" />
</p>


```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # sort by x_end
        points.sort(key = lambda x : x[1])
        
        arrows = 1
        first_end = points[0][1]
        for x_start, x_end in points:
            # if the current balloon starts after the end of another one,
            # one needs one more arrow
            if first_end < x_start:
                arrows += 1
                first_end = x_end
        
        return arrows
```
#### Remark:
- KEY: SORT BY END `points.sort(key = lambda x : x[1])`
#### Submission:
```
Runtime
2670 ms
Beats
45.18%
Memory
59.9 MB
Beats
35.51%
```
#### Complexity:
- Time: O(NlogN)
- Space: O(N) sort since the `list.sort()`function in Python is implemented with the Timsort algorithm whose space complexity is O(N)
