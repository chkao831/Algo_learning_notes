### Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
>You are given an array prices where `prices[i]` is the price of a given stock on the `ith` day.
>
>You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
>
>Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > max_profit:
                max_profit = p - min_price
        return max_profit
```
#### Remark:
- The points of interest are the peaks and valleys in the given graph. We need to find the largest price following each valley, which difference could be the max profit. We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.
#### Submission:
```
Runtime
2394 ms
Beats
52.29%

Memory
25 MB
Beats
87.43%
```
#### Complexity:
- Time: O(N)
- Space: O(1)
