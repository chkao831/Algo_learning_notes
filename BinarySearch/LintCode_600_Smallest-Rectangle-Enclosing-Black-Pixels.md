### Smallest Rectangle Enclosing Black Pixels
https://www.lintcode.com/problem/600/
> An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

<img src="../images/600_Black-Rectangles.jpg" width="500px" />

Intuition: 暴力解 O(m*n),\
or 四次二分
```
0~y find first row
y~m-1 find last row
0~x find first column
x~n-1 find last column
```
其中1,3可以寫成一種二分, 2,4可以寫成第二種二分
```python
```
#### Remark:
- 
#### Submission:
```
```
#### Complexity:
- Time:
- Space:
