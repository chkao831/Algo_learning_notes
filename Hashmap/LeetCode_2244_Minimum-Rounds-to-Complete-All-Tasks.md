### Minimum Rounds to Complete All Tasks
https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/
>You are given a 0-indexed integer array `tasks`, where `tasks[i]` represents the difficulty level of a task. In each round, you can complete **either 2 or 3 tasks** of the same difficulty level.
>
>Return the minimum rounds required to complete all the tasks, or `-1` if it is not possible to complete all the tasks.

<p>
    <img src="https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/solutions/2779140/Figures/2244/2244A.png" width="800" />
</p>

```python
from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        rounds = 0
        for task, freq in counter.items():
            if freq == 1:
                return -1
            elif freq % 3 == 0:
                rounds += freq // 3
            else:
                rounds += freq // 3 + 1
        return rounds
```
#### Remark:
- Key: Figure out the mod 3 pattern
#### Submission:
```
Runtime
2338 ms
Beats
40.17%

Memory
28.5 MB
Beats
44.10%
```
#### Complexity:
- Time: O(N)
- Space: O(N)
