### Best Team With No Conflicts
https://leetcode.com/problems/best-team-with-no-conflicts/
>You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.
>
>However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.
```python
class Solution:

    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        #  scores = [4,4,6,5]
        #  ages = [2,1,5,1]
        #  dp = [0, 0, 0, 0, 0]
        #  score_age = [(4,1), (4,2), (5,1), (6,5)]
        #   score   age     dp
        #                   age=1, 2, 3, 4, 5
        #   –––––  –––––    ––––––––––––––––––
        #     4      1      [0, 4, 0, 0, 0, 0]
        #     4      2      [0, 4, 8, 0, 0, 0]
        #     5      1      [0, 9, 8, 0, 0, 0]
        #     6      5      [0, 9, 8, 0, 0,15] 

        dp = [0]*(1+max(ages))
        score_age = sorted(zip(scores, ages))
        for score, age in score_age:
            dp[age] = score + max(dp[:age+1])                            
        return max(dp)
```
#### Remark:
- 
#### Submission:
```
Runtime
383 ms
Beats
95.80%

Memory
14.3 MB
Beats
51.75%
```
#### Complexity:
- Time: outer loop takes O(N) and max calculation takes O(N) too. So, time complexity should be O(N^2)
- Space: O(N)
