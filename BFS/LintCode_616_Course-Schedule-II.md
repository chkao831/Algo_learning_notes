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
