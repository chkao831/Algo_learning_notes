# Traveling Salesman Problem (TSP)
https://www.lintcode.com/problem/816/
>Give `n` cities (labeled from `1` to `n`), and the undirected road's `cost` among the cities as a three-tuple `[A, B, c]`\
>(i.e there is a road between city `A` and city `B` and the `cost` is `c`). \
>We need to **find the smallest cost to travel all the cities starting from 1**.

- 排列式搜索的典型代表
- 著名的NP問題(non-deterministic polynomial-time)
- DP解法是加分項

## a. 暴力DFS

```python
```
#### Remark:
- graph構建: dict of dict, 邊initialized as float('inf')
#### Submission:
```
```
#### Complexity:
- Time:
- Space:

## b. 暴力DFS + 最優性剪枝 (prunning, or Optimal Prunning Algorithm)

```python
```
#### Remark:
- 
#### Submission:
```
```
#### Complexity:
- Time:
- Space:
