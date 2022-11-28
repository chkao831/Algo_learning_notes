## Functions
#### filter()
**每個元素**
```python
filter(lambda parameter: expression, iterable)
```
#### map()
**每個元素**
```python
map(lambda parameter: expression, iterable)
```
#### reduce()
將可疊代物件中的**前兩個元素**先進行Lambda運算式的運算。
接著將第一個步驟的運算結果和可疊代物件中的下一個元素(第三個)傳入Lambda函式進行運算。
```python
from functools import reduce
reduce(lambda parameter1, parameter2: expression, iterable)
```
#### sorted()
```python
sorted(iterable, key=lambda parameter: expression)
```
#### max()
```python
max(dict, key= lambda x: dict[x]) # find key corresponding to the maximum value
```
#### defaultdict()
`defaultdict` is a dict that creates a default value any time you access it with a non-existent key. It does this by calling the function you pass to it. A common use case is to create a counter by having a `defaultdict` that automatically creates zero values that can then be incremented:
```python
>>> foo = defaultdict(lambda: 0)
>>> foo["bar"]
0
>>> foo["bar"] += 1
>>> foo["bar"]
1
```
Since the function used by a `defaultdict` can be anything, **we can nest them** by giving **an outer dict a function that returns an inner `defaultdict`**:
```python
>>> foo = defaultdict(lambda: defaultdict(lambda: 0))
>>> foo["bar"]["baz"]
0
```

## Examples
```python
from functools import reduce

numbers = [50, 2, 12, 30, 27, 4]
filtered = filter(lambda x: x > 10, numbers) # list(filtered) = [50, 12, 30, 27]
mapped = map(lambda: x: x*2, numbers) # list(mapped) = [100, 4, 24, 60, 54, 8]
reduced = reduce(lambda x, y: x+y, numbers) # reduced = 125

pairs = [('a', 3), ('b', 5), ('c', 1)]
ssorted = sorted(numbers, key=lambda pairs: pairs[1]) # list(ssorted) = [('c', 1), ('a', 3), ('b', 5)]
```

## Application
- [Lint2929](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_2929_Find-the-most-expensive-items.md) - Find the most expensive items
