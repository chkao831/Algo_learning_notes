## Binary Search
  - Intuition: When asked for O(logn) time complexity, think about Binary Search
  - Strategy [破刀式]: When asked for something better than O(n), it usually points to O(logn), Binary Search
  - Binary Search使用了Decrease and Conquer（減治），不屬於分治
  
  - Problem Type
    - a. 寫出不會死循環的二分法 
      - 代表題：[Lint457](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_457_Classical-Binary-Search.md)
        ```
        start <= end
        mid = (start+end)//2
        ```
      - Why judge twice at the end? Would better avoid dead cycle using such a neighboring method. And, need to judge twice since because both pointers are possible to point to the target...
        ```
        [1, 2, 3], target = 3; target is at right pointer
            ^  ^
        [1, 2, 3], target = 1; target is at left pointer
         ^  ^ 
        ```
    - b. 在排序的數組上進行二分 （OO.....OXXXX..., find X) 
      - 代表題：[Lint460](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_460_Find-K-Closest-Elements.md)
      - 建立OOXX模型：
        - 將左半邊有序數組看作O，右邊看作X
        - 設立條件找右邊第一個數
    - c. 在未排序的數組上進行二分
      - 代表題：[Lint75](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_75_Find-Peak-Element.md)
      - 可以根據判斷，留下有解的那一半（去掉無解的那一半） 
    - d. 在答案集上進行二分 [HARD]
      - 代表題：[Lint183](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_183_Wood-Cut.md)
      - step1: 確定答案範圍 -> step 2: 驗證答案大小
      - 本質：求滿足某條件的最大值或最小值，最終結果是個有限的集合，每個結果有個對應的映射，結果集合和映射集合間有正相關或負相關。
      - 手法：在映射結果上進行二分，從而實現對結果集合的二分。
      - Classical scenario: sqrt(x) for x=10, ans=3
        - x^(1/2) = y => x = y^2
        - 3^2 < 10, while 4^2 > 10, so 3 is the last y that satisfies
            
| Item | Type | Topic | Remark | Link(s) |
|  ----  |  ----  | ----  | ----  | ----  |
| 1 | a | 模板及基礎應用 |  | 模板：[Lint457](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_457_Classical-Binary-Search.md); <br/> [Lint458](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_458_Last-Position-of-Target.md)(Last Position) |
| 1' | a | | 結合了first_position, last_position觀念的好題(HARD) | [Lint600](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_600_Smallest-Rectangle-Enclosing-Black-Pixels.md) |
| 2 | b | 排序數組上的二分法 | OOXX<br/>Keywords: target, sorted, equal/close to target | [Lint447](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_447_Search-in-a-Big-Sorted-Array.md)(BigSorted); [Lint460](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_460_Find-K-Closest-Elements.md)+[Leet658](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LeetCode_658_Find-K-Closest-Elements.md)(K-Closest) |
| 2' | b |  | Rotated Sorted Array, OOXX | [Lint159](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_159_Find-Minimum-in-Rotated-Sorted-Array.md)+[Lint160](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_160_Find-Minimum-in-Rotated-Sorted-Array-II.md)(Find-Rotated); [Lint62](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_62_Search-in-Rotated-Sorted-Array.md)+[Lint63](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_63_Search-in-Rotated-Sorted-Array-II.md)(Search-Rotated) |
| 2" | b | | 2D<->1D Binary Search | [Leet74](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LeetCode_74_Search-a-2D-Matrix.md)+[Lint38](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_38_Search-a-2D-Matrix-II.md) |
 | 3 | c | 未排序數組上的二分法 |  | [Lint75](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_75_Find-Peak-Element.md) |
 | 4 | d | 答案集上的二分 | Keywords: 有限可能解, 映射, 正負相關, O(nlogn) | [Lint183](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_183_Wood-Cut.md), [Lint437](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_437_Copy-Books.md) | 
