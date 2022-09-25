### Friend Circles
https://www.lintcode.com/problem/1179/
>There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.
>
>Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.
```python
from typing import (
    List,
)

class Solution:

    def __init__(self):
        self.set_visited = set()

    def find_circle_num(self, m: List[List[int]]) -> int:
        """
        @param m: a matrix
        @return: the total number of friend circles among all the students
        """

        def bfs(student: int):
            queue = collections.deque([student])
            self.set_visited.add(student)
            while queue:
                student = queue.popleft()
                for s in range(len(m)):
                    if s == student: continue
                    if m[student][s] == 1 and s not in self.set_visited:
                        queue.append(s)
                        self.set_visited.add(s)

        if not m or not m[0]:
            return 0
        circles = 0
        for student in range(len(m)):
            if student not in self.set_visited:
                bfs(student)
                circles += 1
        return circles
```
#### Remark:
- Similar to [Lint433-Number_of_Islands](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_433_Number-of-Islands.md)
#### Submission:
```
81 ms
time cost
·
5.96 MB
memory cost
·
Your submission beats
99.00 %
Submissions
```
#### Complexity:
- Time: O(m^2)
- Space: O(m)
