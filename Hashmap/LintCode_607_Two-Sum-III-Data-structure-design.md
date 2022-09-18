https://www.lintcode.com/problem/607/

## Hashmap

```python
class TwoSum:
    def __init__(self):
        self.hashmap = {}
    
    def add(self, number):
        """Add element to hashmap in format of {ele:count}. 
        @param number: An integer
        """
        if number in self.hashmap:
            self.hashmap[number] += 1
        else:
            self.hashmap[number] = 1

    def find(self, value):
        """Find if there exists any pair of numbers which sum is equal to the value.
        @param value: An integer
        @return True if found; False if not found.
        """
        for ele in self.hashmap:
            complement = value - ele
            if complement in self.hashmap and (ele!=complement or self.hashmap[ele]>1):
                return True
        return False
```
#### Remark:
- add() 4 lines could instead be 1 line: `self.hashmap[number] = self.hashmap.get(number, 0) + 1`
#### Submission:
```
674 ms
time cost
·
8.59 MB
memory cost
·
Your submission beats
95.00 %
Submissions
```
#### Complexity:
- Time: add O(1) & find O(n) = total O(n)
- Space: O(n)

## Two Pointers
```python
class TwoSum:
    def __init__(self):
        self.numbers = []
    
    def add(self, number):
        """Add element to list by insertion sort with O(n) time. 
        @param number: An integer
        """
        self.numbers.append(number)
        idx_ptr = len(self.numbers) - 1
        while idx_ptr > 0 and self.numbers[idx_ptr-1] > number:
            self.numbers[idx_ptr-1], self.numbers[idx_ptr] = self.numbers[idx_ptr], self.numbers[idx_ptr-1]
            idx_ptr -= 1

    def find(self, value):
        """Find if there exists any pair of numbers which sum is equal to the value.
        @param value: An integer
        @return True if found; False if not found.
        """
        left, right = 0, len(self.numbers)-1

        while left < right:
            if self.numbers[left] + self.numbers[right] == value:
                return True
            elif self.numbers[left] + self.numbers[right] < value:
                left += 1
            else:
                right -= 1
        return False
```
#### Remark:
- For faster version, see above Hashmap Approach.
#### Submission:
```
Time Limit Exceeded
```
#### Complexity:
- Time: add O(n) (insertion sort) & find O(n) = total O(n)
- Space: O(n)

