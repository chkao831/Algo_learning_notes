### Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/description/
>Given an array of points where `points[i] = [xi, yi]` represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

**Idea:** For a fixed point `points[i]`, consider all other points `points[j]` and calculate the `atan2` for each vector `points[j] - points[i]`. Then find the maximum number of times some angle value occurs among the calculated values. 

<p>
    <img src="https://leetcode.com/problems/max-points-on-a-line/solutions/2910679/Figures/149/149_max_points_on_a_line.drawio.png" width="500" />
</p>

```python
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        result = 2
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(n):
                if j != i:
                    cnt[math.atan2(points[j][1] - points[i][1],
                                   points[j][0] - points[i][0])] += 1
            result = max(result, max(cnt.values()) + 1)
        return result
```
#### Remark:
- The `math.atan2()` method returns the arc tangent of y/x, in radians. Where x and y are the coordinates of a point (x,y).
  - The returned value is between PI and -PI.
  - syntax: `math.atan2(y, x)`
#### Submission:
```
Runtime
114 ms
Beats
77.94%

Memory
14 MB
Beats
53.74%
```
#### Complexity:
- Time: O(n^2)
- Space: O(n) (hashmap storage)
