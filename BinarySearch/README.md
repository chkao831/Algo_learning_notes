## Binary Search
  - Intuition: When asked for O(logn) time complexity, think about Binary Search
  - Strategy [破刀式]: When asked for something better than O(n), it usually points to O(logn), Binary Search
  
  ```
  start <= end
  mid = (start+end)//2
  ```
  - Problem Type
    - 在排序的數組上進行二分 （OO.....OXXXX..., find X) 
      - 建立OOXX模型：
        - 將左半邊有序數組看作O，右邊看作X
        - 設立條件找右邊第一個數
    - 在答案集上進行二分
      - step1: 確定答案範圍 -> step 2: 驗證答案大小
      - Classical: sqrt(x) for x=10, ans=3
        - x^(1/2) = y => x = y^2
        - 3^2 < 10, while 4^2 > 10, so 3 is the last y that satisfies
            
      
 

