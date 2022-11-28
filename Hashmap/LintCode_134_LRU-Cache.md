### LRU Cache
https://www.lintcode.com/problem/134/
>Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: `get` and `set`.
>
>`get(key)` Get the value (will always be positive) of the key if the key exists in the cache, otherwise return `-1`.\
>`set(key, value)` Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.\
>Finally, you need to return the data from each get.

- Cache = Limited size Hashmap
- 淘汰LRU (Least Recently Used)
  - 要支持append(i.e. push back, newest), popleft(i.e. pop front, oldest), pop(x)然後append 
  - 按時間訪問順序來進行的 訪問類型包括get & set
  - `213 -1-> 231 -2-> 312 -2-> 312`
  - 時間先後性：會用到**線性數據結構**
    - 數組(array) 連續型存儲 從左到右
    - 鏈表(linked list) 離散型存儲 更靈活 因為需要讓一個數從中間拿出來放到後面 所以不選擇array(O(n)整體挪動)
  - 要怎麼找到那個特定的數（才可以O(1)快速刪除）？哈希表
    - 用哈希表去存儲他的前繼節點
    - Singly Linked List (單向鏈表)就可以了，要在hash中存儲prev node，如`dummy->1->2->3->null`，`hash[1]=dummy, hash[2]=node1...`
  - 判斷用的東西是key, 其value只是附帶的，要在get(key)時return的產物而已 
<p>
    <img src="https://www.interviewcake.com/images/svgs/lru_cache__chocolate_cake_recipe_request_response.svg?bust=210" width="300" />
</p>

- 把一個功能外包：`def kick(prev)`其需要把一個節點丟出來 然後再扔到尾巴去  
  - pre: `prev->node->next->...->tail`
  - post: `prev->next->...->tail->node` 
  
訪問disk是ns級別的，快; 訪問database(db)是ms級別的，慢。

```python
class LinkedNode:
    def __init__(self, key=None, val=None, nextNode=None):
        self.key = key
        self.val = val
        self.next = nextNode

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.keyToPrev = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity

    def _push_back(self, node):
        """
        ... -> old_tail -> None
        ... -> old_tail -> new_tail -> None
        """
        self.keyToPrev[node.key] = self.tail # to-prev
        self.tail.next = node # to-next
        self.tail = node
        
    def _pop_front(self):
        """
        dummy -> old_front -> new_front -> ...
        dummy -> new_front -> ...
        """
        old_front, new_front = self.dummy.next, self.dummy.next.next
        del self.keyToPrev[old_front.key]
        self.keyToPrev[new_front.key] = self.dummy # to-prev
        self.dummy.next = new_front # to-next

    def _kick(self, prev):
        """
        prev -> node -> next -> ... -> tail
        prev -> next -> ... -> tail -> node
        """
        cur_node = prev.next
        if cur_node == self.tail: # already kicked
            return
        next_node = cur_node.next

        self.keyToPrev[next_node.key] = prev # to-prev
        prev.next = next_node # to-next
        cur_node.next = None
        self._push_back(node=cur_node)

    def get(self, key):
        """
        @param: key: An integer
        @return: An integer
        """
        if key not in self.keyToPrev:
            return -1
        else:
            prev_node = self.keyToPrev[key]
            cur_node = prev_node.next
            self._kick(prev=prev_node)
            return cur_node.val

    def set(self, key, value):
        """
        @param: key: An integer
        @param: value: An integer
        @return: nothing
        """
        if key in self.keyToPrev:
            prev_node = self.keyToPrev[key]
            self._kick(prev=prev_node)
            self.tail.val = value
        else:
            new_node = LinkedNode(key=key, val=value)
            self._push_back(node=new_node)
            # LRUCache
            if len(self.keyToPrev) > self.capacity:
                self._pop_front()
```

#### Remark:
- CPU會把比較常訪問的東西放到L1 cache裡，其位置離CPU較近，訪問速度也較快
- 頻繁錯誤：`self.keyToPrev`的key是Node的key, 不是Node本身; value是Node
#### Submission:
```
1593 ms
time cost
·
16.36 MB
memory cost
·
Your submission beats
34.80 %
Submissions
```
#### Complexity:
- Time:
- Space:
