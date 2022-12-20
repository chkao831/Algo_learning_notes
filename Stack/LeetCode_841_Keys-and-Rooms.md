### Keys and Rooms
https://leetcode.com/problems/keys-and-rooms/description/
>There are `n` rooms labeled from `0` to `n - 1` and all the rooms are locked except for room `0`. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
>
>When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
>
>Given an array rooms where `rooms[i]` is the set of keys that you can obtain if you visited room `i`, return `true` if you can visit all the rooms, or `false` otherwise.


```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = []
        for r0 in rooms[0]:
            stack.append(r0)
        visited = [False]*len(rooms)
        visited[0] = True

        while stack:
            room = stack.pop()
            visited[room] = True
            for r in rooms[room]:
                if visited[r] is True:
                    continue
                stack.append(r)
        return all(visited)
```
#### Remark:
- The `all()` function returns `True` if all items in an iterable are true, otherwise it returns `False`.
#### Submission:
```
Runtime
76 ms
Beats
79.1%

Memory
14.4 MB
Beats
57.55%
```
#### Complexity:
- Time: O(n)
- Space: O(n)
