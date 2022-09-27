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
not deque([[]])!!!
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
