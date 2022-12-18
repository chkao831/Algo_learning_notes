### Daily Temperatures
https://leetcode.com/problems/daily-temperatures/description/
>Given an array of integers temperatures represents the daily temperatures, return an array answer such that `answer[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.
```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        out = [0]*n
        for date, cur_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur_temp:
                d = stack.pop()
                out[d] = date - d
            stack.append(date)
        return out
```
#### Remark:
- The naive/brute-force way to solve this problem is to iterate through the array, and for each day, iterate through all of the remaining days until you find a warmer temperature. This approach would have a time complexity of O(N^2).
- Monotonic Stack
  - use `temperatures[i]` to find the temperature of the `ith` day
  - On each day, there are two possibilities. 
    - If the current day's temperature is not warmer than the temperature on the top of the stack, we can just push the current day onto the stack - since it is not as warm (equal or smaller), this will maintain the sorted property.
    - If the current day's temperature is warmer than the temperature on top of the stack, this is significant. It means that the current day is the first day with a warmer temperature than the day associated with the temperature on top of the stack. 
#### Submission:
```
Runtime
3396 ms
Beats
44.62%

Memory
28.8 MB
Beats
51.76%
```
#### Complexity:
- Time: O(n) (in the worst case, every element will be pushed and popped once. This gives a time complexity of O(2N))
- Space: O(n)
