## Binary Search
  - Intuition: When asked for O(logn) time complexity, think about Binary Search
  - Strategy [破刀式]: When asked for something better than O(n), it usually points to O(logn), Binary Search
  - Binary Search使用了Decrease and Conquer（減治），不屬於分治
  
  ```
  start <= end
  mid = (start+end)//2
  ```
  - Problem Type
    - a. 寫出不會死循環的二分法 
    - b. 在排序的數組上進行二分 （OO.....OXXXX..., find X) 
      - 建立OOXX模型：
        - 將左半邊有序數組看作O，右邊看作X
        - 設立條件找右邊第一個數
    - c. 在未排序的數組上進行二分
      - 可以根據判斷，留下有解的那一半（去掉無解的那一半） 
    - d. 在答案集上進行二分 [HARD]
      - step1: 確定答案範圍 -> step 2: 驗證答案大小
      - 本質：求滿足某條件的最大值或最小值，最終結果是個有限的集合，每個結果有個對應的映射，結果集合和映射集合間有正相關或負相關。
      - 手法：在映射結果上進行二分，從而實現對結果集合的二分。
      - Classical: sqrt(x) for x=10, ans=3
        - x^(1/2) = y => x = y^2
        - 3^2 < 10, while 4^2 > 10, so 3 is the last y that satisfies
            
      
 

