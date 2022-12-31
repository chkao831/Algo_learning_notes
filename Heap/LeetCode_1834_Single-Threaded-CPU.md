### Single-Threaded CPU
https://leetcode.com/problems/single-threaded-cpu/description/
>Return the order in which the CPU will process the tasks.
```python
from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        heap: List[Tuple[int, int]] = [] # minheap
        out: List[int] = []
        
        to_do_tasks = [(enqueue, duration, index) for index, (enqueue, duration) in enumerate(tasks)]
        to_do_tasks.sort()
        to_do_pointer = 0

        current_time = 0
        while to_do_pointer < len(to_do_tasks) or heap:
            # nothing in the heap, and haven't reached time yet
            if not heap and current_time < to_do_tasks[to_do_pointer][0]:
                # heappush(heap, (to_do_tasks[to_do_pointer][1], to_do_tasks[to_do_pointer][2]))
                current_time = to_do_tasks[to_do_pointer][0]
                # to_do_pointer += 1
            # for available item for the current time, push to heap
            while to_do_pointer < len(to_do_tasks) and to_do_tasks[to_do_pointer][0] <= current_time:
                heappush(heap, (to_do_tasks[to_do_pointer][1], to_do_tasks[to_do_pointer][2]))
                to_do_pointer += 1
            duration, out_idx = heappop(heap)
            current_time += duration
            out.append(out_idx)
        return out
```
#### Remark:
- When nothing in the heap, and haven't reached time yet, just increment time to the nearest available timing. Don't push!!!
#### Submission:
```
Runtime
2034 ms
Beats
66.22%

Memory
63 MB
Beats
37.4%
```
#### Complexity:
- Time: O(nlogn)
- Space: O(n)
