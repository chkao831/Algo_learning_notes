




### Course Schedule II
https://www.lintcode.com/problem/616/
>There are a total of n courses you have to take, labeled from `0` to `n - 1`.
>
>Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
>
>Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
>
>There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

```python
from typing import (
    List,
)

class Solution:

    def find_order(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        @param num_courses: a total of n courses
        @param prerequisites: a list of prerequisite pairs
        @return: the course order
        """    
        def generate_dict():
            self.dict_prereq_to_req = {c: [] for c in range(0, num_courses)}
            self.dict_course_inDegree = {c: 0 for c in range(0, num_courses)}
            for latter, former in prerequisites:
                self.dict_prereq_to_req[former] = self.dict_prereq_to_req.get(former, []) + [latter]
                self.dict_course_inDegree[latter] = self.dict_course_inDegree.get(latter, 0) + 1
        
        generate_dict()
        order = []
        queue = collections.deque([c for c in self.dict_course_inDegree if self.dict_course_inDegree[c]==0])
        while queue:
            course = queue.popleft()
            order.append(course)
            for req in self.dict_prereq_to_req[course]:
                self.dict_course_inDegree[req] -= 1
                if self.dict_course_inDegree[req] == 0:
                    queue.append(req)
                    
        if len(order)!=num_courses: 
            return []
        else: 
            return order
```
#### Remark:
- 
#### Submission:
```
860 ms
time cost
·
65.52 MB
memory cost
·
Your submission beats
16.20 %
Submissions
```
#### Complexity:
- 假設n個點，m條邊；
     - 記錄拓撲序空間複雜度為O(n)，記錄入度最壞複雜度為O(n)，空間複雜度O(n)；
     - 記錄每個點的入度為O(m)，拓撲排序為O(m)，時間複雜度O(m)。

