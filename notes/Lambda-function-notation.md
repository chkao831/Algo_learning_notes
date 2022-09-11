#### Define lambda function, then apply to argument
```python
lamb_multiply = lambda x, y: x*y # lambda parameter: expression
print(lamb_multiply(4, 2)) # 8
```
#### IIFE(immediately invoked function expression)
```python
print((lambda x, y: x*y)(4, 2)) # (lambda parameter: expression)(argument)
```
