## Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
>You are given an integer array prices where `prices[i]` is the price of a given stock on the `it`h day.
>
>On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
>
>Find and return the maximum profit you can achieve.

### Peak Valley Approach

<p>
    <img src="https://leetcode.com/media/original_images/122_maxprofit_1.PNG" width="600" />
</p>

```python
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        valley = peak = sys.maxsize
        for p in prices:
            if p < peak:
                total_profit += (peak - valley)
                valley = peak = p
            else: # p >= peak
                peak = p
        # may end up in the second loop
        total_profit += (peak - valley)
        return total_profit
```
#### Remark:
- The key point is we need to consider every peak immediately following a valley to maximize the profit. 
#### Submission:
```
Runtime
61 ms
Beats
95.4%

Memory
15.2 MB
Beats
69.49%
```
#### Complexity:
- Time: O(N)
- Space: O(1)

### Simple One Pass

<p>
    <img src="https://leetcode.com/media/original_images/122_maxprofit_2.PNG" width="600" />
</p>

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                total_profit += (prices[i]-prices[i-1])
        return total_profit
```
#### Remark:
- In this case, instead of looking for every peak following a valley, we can simply go on crawling over the slope and keep on adding the profit obtained from every consecutive transaction.
#### Submission:
```
Runtime
75 ms
Beats
76.69%

Memory
15.2 MB
Beats
25.38%
```
#### Complexity:
- Time: O(N)
- Space: O(1)
