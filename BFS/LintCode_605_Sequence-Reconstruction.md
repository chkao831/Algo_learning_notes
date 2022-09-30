### Sequence Reconstruction

https://www.lintcode.com/problem/605/description

```python
from typing import (
    List,
)
from collections import defaultdict

class Solution:
    
    def __init__(self):
        self.dict_indeg = defaultdict(int)
        self.dict_seq = defaultdict(set)

    def sequence_reconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        """
        @param org: a permutation of the integers from 1 to n
        @param seqs: a list of sequences
        @return: true if it can be reconstructed only one or false
        """    

        def generate_dict_seq():
            for seq in seqs:
                if len(seq)==1 and seq[0] not in org:
                    self.dict_seq[seq[0]].update(org)
                for idx in range(1, len(seq)):
                    self.dict_seq[seq[idx-1]].add(seq[idx])

        def generate_dict_ind():
            for o in org:
                self.dict_indeg[o] = 0
            for key, vals in self.dict_seq.items():
                for val in vals:
                    self.dict_indeg[val] += 1

        if not org: return True
        if not any(seqs): return False

        generate_dict_seq()
        generate_dict_ind()

        queue, order = collections.deque([q for q in self.dict_indeg if self.dict_indeg[q]==0]), []
        while queue:
            if len(queue) != 1:
                return False
            ele = queue.popleft()
            order.append(ele)
            for next_ele in self.dict_seq[ele]:
                self.dict_indeg[next_ele] -= 1
                if self.dict_indeg[next_ele] == 0:
                    queue.append(next_ele)
                    
        return True if order == org else False
```

```
[5,3,2,4,1]
[[5,3,2,4],[4,1],[1],[3],[2,4], [1000000000]]
```
#### Remark:
- 題目描述不全：
    - 遇到org是空的情況 return True
    - 遇到seqs全空的情況`[[], []]` 用`any`判斷 然後return False
- 遇到這種case
    `org = [5,3,2,4,1], seqs = [[5,3,2,4],[4,1],[1],[3],[2,4], [1000000000]]`
    - seqs裡有單獨seq只有一個元素的 這種不會被`generate_dict_seq`處理好關係。對於`[1000000000]`只有一個元素 並且在org完全沒出現的，選擇把整個org都變成了他的subsequence, 這樣後續一定會報False。
- 善用`defaultdict`!!!
    - `self.dict_indeg = defaultdict(int)`
    - `self.dict_seq = defaultdict(set)`
#### Submission:
```
143 ms
time cost
·
10.37 MB
memory cost
·
Your submission beats
41.20 %
Submissions
```
#### Complexity:
- Time: O(N)
- Space: O(N)
