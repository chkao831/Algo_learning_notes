## Lowest Common Ancestor of a Binary Tree
https://www.lintcode.com/problem/88/
>給定二叉樹的根節點和兩個子節點，找到兩個節點的最近公共父節點(LCA)。最近公共祖先是兩個節點的公共的祖先節點且具有最大深度。
>
>**假設給出的兩個節點都在樹中存在**


### 方法: 分治法 + 有啥return啥
定義返回值：
- [最優先] AB都存在 -> return LCA(A,B)
- 只有A -> return A
- 只有B -> return B
- AB都不存在 -> return None
```python
        @param: root: The root of the tree
        @param: root: The root of the tree
```
#### Remark:
- 
#### Submission:
```

```
#### Complexity:
- Time: O(n)
- Space: O(h) ~O(n)

### 方法: 直接遍歷
找出兩個節點之間深度最小的節點
- 優：支持多次在線查詢(Online Algorithm)
- 劣：會走到（多次）重複的路
不用知道怎麼寫，但知道有這個概念就好。

<img src="../images/88_LCA_traversal.png” width=“300" />
