### Course Schedule
https://www.lintcode.com/problem/615/
>There are a total of n courses you have to take, labeled from `0` to `n - 1`.
>
>Before taking some courses, you need to take other courses. For example, to learn course 0, you need to learn course 1 first, which is expressed as [0,1].
> 
>Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
>
>**Prerequisites may appear duplicated**

```python
from typing import (
    List,
)

class Solution:
    
    def __init__(self):
        self.dict_course_to_prereq = {}
        self.dict_course_inDegree = {}

    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        """
        @param num_courses: a total of n courses
        @param prerequisites: a list of prerequisite pairs
        @return: true if can finish all courses or false
        """
        
        def generate_dict():
            self.dict_prereq_to_req = {c: [] for c in range(0, num_courses)}
            self.dict_course_inDegree = {c: 0 for c in range(0, num_courses)}
            for latter, former in prerequisites:
                self.dict_prereq_to_req[former] = self.dict_prereq_to_req.get(former, []) + [latter]
                self.dict_course_inDegree[latter] = self.dict_course_inDegree.get(latter, 0) + 1

        generate_dict()
        starting_courses = [c for c in self.dict_course_inDegree if self.dict_course_inDegree[c]==0]
        queue, queue_count = collections.deque(starting_courses), 0 # not deque([[]])!!!
        while queue:
            course = queue.popleft()
            queue_count += 1
            for req in self.dict_prereq_to_req[course]:
                self.dict_course_inDegree[req] -= 1
                if self.dict_course_inDegree[req] == 0:
                    queue.append(req)
        return queue_count == num_courses
```
#### Remark:
- not `deque([starting_courses])` because `starting_courses` is already a list of items
#### Submission:
```
821 ms
time cost
·
70.21 MB
memory cost
·
Your submission beats
7.20 %
Submissions
```
#### Complexity:
- 假設n個點，m條邊；
     - 記錄拓撲序空間複雜度為O(n)，記錄入度最壞複雜度為O(n)，空間複雜度O(n)；
     - 記錄每個點的入度為O(m)，拓撲排序為O(m)，時間複雜度O(m)。
