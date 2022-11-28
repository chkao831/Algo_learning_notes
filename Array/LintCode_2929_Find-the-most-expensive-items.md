### Find the most expensive items
https://www.lintcode.com/problem/2929/description
>給定一個商品列表 goods，這個列表中存儲的是多個商品元組，每個元組有兩個元素，分別代表著商品名，商品價格，請你按照價格將整個商品列表排序，如果價格相同按照商品名字典序排序，然後將價格最貴的商品名返回。
```python
def get_goods(goods: list) -> str:
    # sort in place
    goods.sort(reverse=True, key=lambda x: x[0]) # lexi, z-a
    goods.sort(reverse=True, key=lambda x: x[1]) # price, high-low
    return goods[0][0]
```
#### Submission:
```
570 ms
time cost
·
5.42 MB
memory cost
·
Your submission beats
14.00 %
Submissions
```
```python
def get_goods(goods: list) -> str:
    sorted_goods = sorted(goods, key=lambda x: (x[1], x[0])) # low-high, a-z
    return sorted_goods[-1][0]
```
#### Submission:
```
548 ms
time cost
·
5.60 MB
memory cost
·
Your submission beats
29.00 %
Submissions
```
