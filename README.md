# Algorithm Learning Notes
> Since Sep 10, 2022\
> Last Updated on Feb 2, 2023

## Language
Python3

## Categories
#### Algorithms
- [Two pointers（雙指針）](https://github.com/chkao831/Algo_learning_notes/tree/main/Two-pointers)
- [Divide-and-Conquer（DnC, 分治）](https://github.com/chkao831/Algo_learning_notes/tree/main/DnC) (including Quick Sort, Quick Select, Merge Sort, etc.)
- [Binary Search（二分法）](https://github.com/chkao831/Algo_learning_notes/tree/main/BinarySearch)
- [Breadth First Search (BFS, 寬度優先搜索)](https://github.com/chkao831/Algo_learning_notes/tree/main/BFS)
- [Depth First Search (DFS, 深度優先搜索）](https://github.com/chkao831/Algo_learning_notes/tree/main/DFS)
- [Operator](https://github.com/chkao831/Algo_learning_notes/tree/main/Operator)
- [Dynamic Programming（DP, 動態規劃）](https://github.com/chkao831/Algo_learning_notes/tree/main/DP)
- Sorting（排序）
  | Type | Average Time | Space | Algorithm Demo | Application | 
  |  ----  | ----  | ----  | ----  | ----  | 
  | Insertion Sort | O(n^2) | O(1) | [Leet147](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_147_Insertion-Sort-List.md) | 1. [[Lint607](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_607_Two-Sum-III-Data-structure-design.md)] Add number with Insertion Sort to the last, then swap to front with O(n) time. |
  | Quick Sort | O(nlogn) | O(logn) | [Lint464](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_464_Sort-Integers-II_QuickSort.md) | 1. [[Lint31](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_31_Partition-Array.md)] Partition highly resembles Quick Sort, except that the left-right partition is strict.<br/>2. [[Lint143](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_143_Sort-Colors-II.md)] Recursion highly resembles Quick Sort, while the pivot (middle color) partition is strict.|
  | Quick Select | O(n) | O(1) | [Leet215](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LeetCode_215_Kth-Largest-Element-in-an-Array_QuickSelect.md) | Quick Select highly resembles [Quick Sort](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_464_Sort-Integers-II_QuickSort.md), except that one knows which part to search for the subsequent recursive call, so the time complexity reduces to O(n). |
  | Merge Sort | O(nlogn) | O(n) | [Leet913](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LeetCode_913_Sort-an-Array.md) | |
  | External Sorting (外排序算法) | | | [Text](https://github.com/chkao831/Algo_learning_notes/blob/main/notes/backup_CH48text.md) | [Repo](https://github.com/chkao831/Algo_learning_notes/tree/main/ExternalSorting) |
  
 #### Data Structures
- [Hashmap (哈希表)](https://github.com/chkao831/Algo_learning_notes/tree/main/Hashmap)
- [Array (數組)](https://github.com/chkao831/Algo_learning_notes/tree/main/Array)
- [Linked List (鏈表)](https://github.com/chkao831/Algo_learning_notes/tree/main/LinkedList)
- [Queue（隊列）](https://github.com/chkao831/Algo_learning_notes/tree/main/Queue)
- [Heap（堆）](https://github.com/chkao831/Algo_learning_notes/tree/main/Heap)
- [Stack（棧）](https://github.com/chkao831/Algo_learning_notes/tree/main/Stack)

#### Notes
- [Stack Space vs. Heap Space](https://chkao831.github.io/files/algo/StackVSHeap.pdf)
- [Complexity Analyses](https://chkao831.github.io/files/algo/Some_complexity_analyses.pdf)
- [Lambda Function Application](https://github.com/chkao831/Algo_learning_notes/blob/main/notes/Lambda-function-application.md)

## Problems (indexed in ascending order)
#### LeetCode
| Index | Topic | Difficulty | Link(s) |
|  ----  | ----  | ----  | ----  |
| 1 | Two Sum | Easy | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_1_Two-Sum.md); <br/>[Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_1_Two-sum.md)|
| 18 | 4Sum | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_18_4Sum.md)|
| 31 | Next Permutation | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_31_Next-Permutation.md) (Iterative) | 
| 51 | N-Queens | Hard | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_51_N-Queens.md) |
| 55 | Jump Game | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_55_Jump-Game.md) |
| 62 | Unique Path | Medium | [DP](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LeetCode_62_Unique-Paths.md) |
| 74 | Search a 2D Matrix | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LeetCode_74_Search-a-2D-Matrix.md) | 
| 86 | Partition List | Medium | [LinkedList](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_86-Partition-List.md) |
| 91 | Decode Ways | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_91_Decode-Ways.md) |
| 94 | Binary Tree Inorder Traversal | Easy | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_94_Binary-Tree-Inorder-Traversal.md) |
| 100 | Same Tree | Easy | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_100_Same-Tree.md) |
| 102 | Binary Tree Level Order Traversal | Medium | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LeetCode_102_Binary-Tree-Level-Order-Traversal.md) |
| 104 | Maximum Depth of Binary Tree | Easy | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_104_Maximum-Depth-of-Binary-Tree.md) |
| 110 | Balanced Binary Tree | Easy | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_110_Balanced-Binary-Tree.md) |
| 120 | Triangle | Medium | [DFS/DP](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LeetCode_120_Triangle.md) |
| 121 | Best Time to Buy and Sell Stock | Easy | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LeetCode_121_Best-Time-to-Buy-and-Sell-Stock.md) |
| 122 | Best Time to Buy and Sell Stock II | Medium | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LeetCode_122_Best-Time-to-Buy-and-Sell-Stock-II.md) |
| 124 | Binary Tree Maximum Path Sum | Hard | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_124_Binary%20Tree-Maximum-Path-Sum.md) |
| 134 | Gas Station | Medium | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LeetCode_134_Gas-Station.md) | Medium |
| 144 | Binary Tree Preorder Traversal | Easy | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_144_Binary-Tree-Preorder-Traversal.md) |
| 145 | Binary Tree Postorder Traversal | Easy | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_145_Binary-Tree-Postorder-Traversal.md) | 
| 147 | Insertion Sort List | Medium | [LinkedList](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_147_Insertion-Sort-List.md) |
| 149 | Max Points on a Line | Hard | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_149_Max-Points-on-a-Line.md) |
150 | Evaluate Reverse Polish Notation | Medium | [Stack](https://github.com/chkao831/Algo_learning_notes/blob/main/Stack/LeetCode_150_Evaluate-Reverse-Polish-Notation.md) |
| 155 | Min Stack | Medium | [Stack](https://github.com/chkao831/Algo_learning_notes/blob/main/Stack/LeetCode_155_Min-Stack.md) |
| 173 | Binary Search Tree Iterator | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_173_Binary-Search-Tree-Iterator.md) |
| 198 | House Robber | Medium | [DP](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LeetCode_198_House-Robber.md) |
| 215 | Kth Largest Element in an Array | Medium | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LeetCode_215_Kth-Largest-Element-in-an-Array_QuickSelect.md)|
| 225 | Implement Stack using Queues | Easy | [Queue](https://github.com/chkao831/Algo_learning_notes/blob/main/Queue/LeetCode_225_Implement-Stack-using-Queues.md) |
| 230 | Kth Smallest Element in a BST | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_230_Kth-Smallest-Element-in-a-BST.md) |
| 232 | Implement Queue using Stacks | Medium | [Stack](https://github.com/chkao831/Algo_learning_notes/blob/main/Stack/LeetCode_232_Implement-Queue-using-Stacks.md) |
| 257 | Binary Tree Paths | Easy | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_257_Binary-Tree-Paths.md) |
| 259 | 3Sum Smaller | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_259_3Sum-Smaller.md)|
| 263 | Ugly Number | Easy | [Array](https://github.com/chkao831/Algo_learning_notes/blob/8b01966f0d4aaabc6c934cc202b0f403cacbac0e/Array/LeetCode_263_Ugly-Number.md) |
| 264 | Ugly Number II | Medium | [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LeetCode_264_Ugly-Number-II.md) |
| 270 | Closest Binary Search Tree Value I | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_270_Closest-Binary-Search-Tree-Value.md) |
| 272 | Closest Binary Search Tree Value II | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_272_Closest-Binary-Search-Tree-Value-II.md) |
| 290 | Word Pattern | Easy | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_290_Word-Pattern.md) |
| 309 | Best Time to Buy and Sell Stock with Cooldown | Medium | [DP](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LeetCode_309_Best-Time-to-Buy-and-Sell-Stock-with-Cooldown.md) |
| 328 | Odd Even Linked List | Medium | [LinkedList](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_328_Odd-Even-Linked-List.md) |
| 380 | Insert Delete GetRandom O(1) | Medium | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_380_Insert-Delete-GetRandom-O(1).md) |
| 451 | Sort Characters By Frequency | Medium | [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LeetCode_451_Sort-Characters-By-Frequency.md) |
| 454 | 4Sum II | Medium | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_454_4Sum-II.md)|
| 611 | Valid Triangle Number | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_611_Valid-Triangle-Number.md)|
| 658 | Find K Closest Elements | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LeetCode_658_Find-K-Closest-Elements.md) | 
| 716 | Max Stack | Hard | [Stack](https://github.com/chkao831/Algo_learning_notes/blob/main/Stack/LeetCode_716_Max-Stack.md) |
| 739 | Daily Temperatures | Medium | [Stack](https://github.com/chkao831/Algo_learning_notes/blob/main/Stack/LeetCode_739_Daily-Temperatures.md) |
| 763 | Partition Lables | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_763_Partition-Labels.md) |
| 834 | Sum of Distances in Tree | Hard | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_834_Sum-of-Distances-in-Tree.md) |
| 872 | Leaf-Similar Trees | Easy | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_872_Leaf-Similar-Trees.md) |
| 886 | Possible Bipartition | Medium | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LeetCode_886_Possible-Bipartition.md) |
| 913 | Sort an Array | Medium | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LeetCode_913_Sort-an-Array.md) |
| 922 | Sort Array By Parity II | Easy | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_922_Sort-Array-By-Parity-II.md) |
| 931 | Minimum Falling Path Sum | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_931_Minimum-Falling-Path-Sum.md) |
| 953 |  Verifying an Alien Dictionary | Easy | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_953_Verifying-an-Alien-Dictionary.md) |
| 980 | Unique Paths III | Hard | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_980_Unique-Paths-III.md) |
| 1026 | Maximum Difference Between Node and Ancestor | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_1026_Maximum-Difference-Between-Node-and-Ancestor.md) |
| 1061 | Lexicographically Smallest Equivalent String | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_1061_Lexicographically-Smallest-Equivalent-String.md) |
| 1071 | Greatest Common Divisor of Strings | Easy | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LeetCode_1071_Greatest-Common-Divisor-of-Strings.md) |
| 1120 | Maximum Average Subtree | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_1120_Maximum-Average-Subtree.md) |
| 1143 | Longest Common Subsequence | Medium | [DP](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LeetCode_1143_Longest-Common-Subsequence.md) |
| 1339 | Maximum Product of Splitted Binary Tree | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_1339_Maximum-Product-of-Splitted-Binary-Tree.md) |
| 1429 | First Unique Number (online algo) | Medium | [LinkedList](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_1429_First-Unique-Number.md) |
| 1443 | Minimum Time to Collect All Apples in a Tree | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_1443_Minimum-Time-to-Collect-All-Apples-in-a-Tree.md) |
| 1519 | Number of Nodes in the Sub-Tree With the Same Label | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_1519_Number-of-Nodes-in-the-Sub-Tree-With-the-Same-Label.md) |
| 1626 | Best Team With No Conflicts | Medium | [DP](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LeetCode_1626_Best-Team-With-No-Conflicts.md) |
| 1834 | Single-Threaded CPU | Medium | [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LeetCode_1834_Single-Threaded-CPU.md) |
| 1962 | Remove Stones to Minimize the Total | Medium | [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LeetCode_1962_Remove-Stones-to-Minimize-the-Total.md) |
| 2161 | Partition Array According to Given Pivot | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_2161_Partition-Array-According-to-Given-Pivot.md) |
| 2031 | Count Subarrays With More Ones Than Zeros | Medium | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LeetCode_2031_Count-Subarrays-With-More-Ones-Than-Zeros.md) |
| 2244 | Minimum Rounds to Complete All Tasks | Medium | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_2244_Minimum-Rounds-to-Complete-All-Tasks.md) |
| 2246 | Longest Path With Different Adjacent Characters | Hard | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_2246_Longest-Path-With-Different-Adjacent-Characters.md) |
| 2256 | Minimum Average Difference | Medium | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LeetCode_2256_Minimum-Average-Difference.md) |
| 2279 | Maximum Bags With Full Capacity of Rocks | Medium | [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LeetCode_2279_Maximum-Bags-With-Full-Capacity-of-Rocks.md) |
| 2389 | Longest Subsequence With Limited Sum | Easy | [BinarySearch](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LeetCode_2389_Longest-Subsequence-With-Limited-Sum.md) |
| 2449 | Minimum Number of Operations to Make Arrays Similar | Hard | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LeetCode_2449_Minimum-Number-of-Operations-to-Make-Arrays-Similar.md) |

#### LintCode
| Index | Topic | Difficulty | Link(s) |
|  ----  | ----  | ----  | ----  |
| 6 | Merge Two Sorted Arrays | Easy | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_6_Merge-Two-Sorted-Arrays.md) |
| 7 | Serialize and Deserialize Binary Tree | Medium | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_7_Serialize-and-Deserialize-Binary-Tree.md) |
| 10 | String Permutation II | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_10_String-Permutation-II.md) |
| 11 | Search Range in Binary Search Tree  | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_11_Search-Range-in-Binary-Search-Tree.md) |
| 13 | Implement strStr() | Naive | [Two Pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_13_Implement-strStr().md) |
| 15 | Permutations | Medium | DFS ([Recursive](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_15_Permutations.md#dfs-recursive-approach)/[Iterative](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_15_Permutations.md#dfs-%E9%9D%9E%E9%81%9E%E6%AD%B8%E7%9A%84%E6%96%B9%E5%BC%8F%E5%AF%A6%E7%8F%BE%E6%8E%92%E5%88%97%E5%92%8C%E7%B5%84%E5%90%88%E9%A1%9Edfs)) |
| 16 | Permutations II | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_16_Permutations-II.md) |
| 18 | Subsets II | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_18_Subsets-II.md) |
| 17 | Subsets | Medium | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_17_Subsets.md#bfs); [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_17_Subsets.md#dfs); [Binary Operator](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_17_Subsets.md#binary-operator) | 
| 31 | Partition Array | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_31_Partition-Array.md) |
| 38 | Search a 2D Matrix II | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_38_Search-a-2D-Matrix-II.md) | 
| 49 | Sort Letters by Case | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/tree/main/Two-pointers) |
| 57 | 3Sum | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_57_3Sum.md) |
| 62 | Search in Rotated Sorted Array | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_62_Search-in-Rotated-Sorted-Array.md) |
| 63 | Search in Rotated Sorted Array II | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_63_Search-in-Rotated-Sorted-Array-II.md) |
| 64 | Merge Sorted Array | Easy | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_64_Merge-Sorted-Array.md) |
| 65 | Median of two Sorted Arrays | Hard | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_65_Median-of-two-Sorted-Arrays.md) |
| 75 | Find Peak Element | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_75_Find-Peak-Element.md) |
| 80 | Median | Medium | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_80_Median.md) |
| 85 | Insert Node in a Binary Search Tree | Easy | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_85_Insert-Node-in-a-Binary-Search-Tree.md) |
| 88 | Lowest Common Ancestor of a Binary Tree | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_88_Lowest-Common-Ancestor-of-a-Binary-Tree.md) |
| 90 | k Sum II | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_90_k-Sum-II.md) |
| 95 | Validate Binary Search Tree | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_95_Validate-Binary-Search-Tree.md) |
| 101 | Remove Duplicates from Sorted Array II | Easy | [Two Pointer](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_101_Remove-Duplicates-from-Sorted-Array-II.md) |
| 104 | Merge K Sorted Lists | Medium | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_104_Merge-K-Sorted-Lists.md)(Heap/PairwiseMerge/MergeSort) |
| 121 | Word Ladder II | Hard | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_121_Word-Ladder-II.md) |
| 120 | Word Ladder | Hard | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_120_Word-Ladder.md) |
| 127 | Topological Sorting | Medium | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_127_Topological-Sorting.md) |
| 128 | Hash Function | Easy | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LintCode_128_Hash-Function.md) | 
| 129 | Rehashing | Medium | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LintCode_129_Rehashing.md) |
| 130 | Heapify | Medium | [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LintCode_130_Heapify.md) |
| 132 | Word Search II | Hard | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_132_Word-Search-II.md) |
| 134 | LRU Cache | Hard | [LinkedList(Hash)](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LintCode_134_LRU-Cache.md) |
| 135 | Combination Sum | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_135_Combination-Sum.md) |
| 137 | Clone Graph | Medium | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_137_Clone-Graph.md) |
| 143 | Sort Colors II | Medium | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_143_Sort-Colors-II.md) | 
| 144 | Interleaving Positive and Negative Numbers | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_144_Interleaving-Positive-and-Negative-Numbers.md) |
| 148 | Sort Colors | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_148_Sort-Colors.md) | 
| 159 | Find Minimum in Rotated Sorted Array | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_159_Find-Minimum-in-Rotated-Sorted-Array.md) |
| 160 | Find Minimum in Rotated Sorted Array II | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_160_Find-Minimum-in-Rotated-Sorted-Array-II.md) |
| 165 | Merge Two Sorted Lists | Easy | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_165_Merge-Two-Sorted-Lists.md) |
| 172 | Remove Element | Easy | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_172_Remove-Element.md) |
| 175 | Invert Binary Tree | Easy | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_175_Invert-Binary-Tree.md) |
| 178 | Graph Valid Tree | Medium | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_178_Graph-Valid-Tree.md) | 
| 183 | Wood Cut | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_183_Wood-Cut.md) |
| 197 | Permutation Index | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_197_Permutation-Index.md) (Iterative) |
| 373 | Partition Array by Odd and Even | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_373_Partition-Array-by-Odd-and-Even.md) |
| 407 | Plus One | Easy | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_407_Plus-One.md) |
| 415 | Valid Palindrome | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_415_Valid-Palindrome.md) |
| 425 | Letter Combinations of a Phone Number | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_425_Letter-Combinations-of-a-Phone-Number.md) |
| 431 | Connected Component in Undirected Graph | Medium | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_431_Connected-Component-in-Undirected-Graph.md) |
| 433 | Number of Islands | Medium | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_433_Number-of-Islands.md) |
| 437 | Copy Books | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_437_Copy-Books.md) |
| 447 | Search in a Big Sorted Array | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_447_Search-in-a-Big-Sorted-Array.md) |
| 453 | Flatten Binary Tree to Linked List | Easy | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_453_Flatten-Binary-to-Linked-List.md) |
| 457 | Classical Binary Search | Easy | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_457_Classical-Binary-Search.md) |
| 458 | Last Position of Target | Easy | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_458_Last-Position-of-Target.md) | 
| 460 | Find K Closest Elements | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_460_Find-K-Closest-Elements.md) | 
| 464 | Sort Integers II | Easy | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_464_Sort-Integers-II_QuickSort.md) |
| 471 | Top K Frequent Words | Medium | [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LintCode_471_Top-K-Frequent-Words.md) |
| 474 | Lowest Common Ancestor II | Easy | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_474_Lowest-Common-Ancestor-II.md) |
| 479 | Second Max of Array | Easy | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_479_Second-Max-of-Array.md) |
| 492 | Implement Queue by Linked List | Easy | [Queue](https://github.com/chkao831/Algo_learning_notes/blob/main/Queue/LintCode_492_Implement-Queue-by-Linked-List.md) |
| 493 | Implement Queue by Linked List II | Easy | [Queue](https://github.com/chkao831/Algo_learning_notes/blob/main/Queue/LintCode_493_Implement-Queue-by-Linked-List-II.md) |
| 514 | Paint Fence | Easy | [DP](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LintCode_514_Paint-Fence.md) |
| 539 | Move Zeroes | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_539_move-zeroes.md) | 
| 545 | Top k Largest Numbers II | Medium | [QuickSelect](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LintCode_545_Top-k-Largest-Numbers-II.md#quick-select--sort-top-k--on--klogk-topk-o1-add); [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LintCode_545_Top-k-Largest-Numbers-II.md#heap--onlogk-topk-ologn-add) |
| 547 | Intersection of Two Arrays | Easy | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_547_Intersection-of-Two-Arrays.md)(TwoPointers/BinarySearch) |
| 548 | Intersection of Two Arrays II | Easy | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_548_Intersection-of-Two-Arrays-II.md)(Hashmap/TwoPointers) |
| 573 | Build Post Office II | Hard | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_573_Build-Post-Office-II.md) |
| 577 | Merge K Sorted Interval Lists | Medium | [ExternalSorting(Heap)](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_577_Merge-K-Sorted-Interval-Lists.md) |
| 578 | Lowest Common Ancestor III | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_578_Lowest-Common-Ancestor-III.md) |
| 585 | Maximum Number in Mountain Sequence | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_585_Maximum-Number-in-Mountain-Sequence.md) |
| 596 | Minimum Subtree | Easy | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_596_Minimum-Subtree.md) |
| 598 | Zombie in Matrix | Medium | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_598_Zombie-in-Matrix.md) |
| 600 | Smallest Rectangle Enclosing Black Pixels | Hard | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_600_Smallest-Rectangle-Enclosing-Black-Pixels.md) |
| 605 | Sequence Reconstruction | Medium | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_605_Sequence-Reconstruction.md) |
| 607 | Two Sum III - Data structure design | Easy | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_607_Two-Sum-III-Data-structure-design.md); <br/>[Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LintCode_607_Two-Sum-III-Data-structure-design.md) |
| 609 | Two sum - Less than or equal to target | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_609_Two-Sum-Less-than-or-equal-to-target.md) |
| 611 | Knight Shortest Path | Medium | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_611_Knight-Shortest-Path.md) | 
| 612 | K Closest Points | Medium | [QuickSelect](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LintCode_612_K-Closest-Points.md#quick-select--sort-top-k--on--klogk); [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LintCode_612_K-Closest-Points.md#heap--onlogk) |
| 615 | Course Schedule | Medium | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_615_Course-Schedule.md) | 
| 616 | Course Schedule II | Medium | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_616_Course-Schedule-II.md) | 
| 618 | Search Graph Nodes | Medium | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_618_Search-Graph-Nodes.md) | 
| 625 | Partition Array II | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_625_Partition-Array-II.md) |
| 628 | Maximum Subtree | Easy | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_628_Maximum-Subtree.md) |
| 630 | Knight Shortest Path II | Medium | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_630_Knight-Shortest-Path-II.md) |
| 654 | Sparse Matrix Multiplication | Medium | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_654_Sparse-Matrix-Multiplication.md) |
| 685 | First Unique Number in Data Stream (offline algo) | Medium |  [Queue](https://github.com/chkao831/Algo_learning_notes/blob/main/Queue/LintCode_685_First-Unique-Number-in-Data-Stream.md) |
| 689 | Two Sum IV - Input is a BST | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_689_Two-Sum-IV-Input-is-a-BST.md) |
| 701 | Trim a Binary Search Tree | Medium | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_701_Trim-a-Binary-Search-Tree.md) |
| 716 | Add and Search | Easy | [Two Pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_716_Add-and-Search.md);<br/>[Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LintCode_716_Add-and-Search.md) |
| 790 | Domino and Tromino Tiling | Medium | [DP](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LeetCode_790_Domino-and-Tromino-Tiling.md) |
| 792 | Kth Prime Number | Easy | [Operator](https://github.com/chkao831/Algo_learning_notes/blob/main/Operator/LintCode_792_Kth-Prime-Number.md) |
| 793 | Intersection of Arrays | Medium | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_793_Intersection-of-Arrays.md)(Hashmap/Heap) |
| 802 | Sudoku Solver | Hard | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_802_Sudoku-Solver.md) |
| 816 | Traveling Salesman Problem (TSP) | Hard | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_816_Traveling-Salesman-Problem.md) |
| 839 | Merge Two Sorted Interval Lists | Easy | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_839_Merge-Two-Sorted-Interval-Lists.md) |
| 841 | Keys and Rooms | Medium | [Stack](https://github.com/chkao831/Algo_learning_notes/blob/main/Stack/LeetCode_841_Keys-and-Rooms.md) |
| 868 | Maximum Average Subarray | Easy | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_868_Maximum-Average-Subarray.md) |
| 891 | Valid Palindrome II | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_891_Valid-Palindrome-II.md) |
| 892 | Alien Dictionary | Hard | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_892_Alien-Dictionary.md) | 
| 924 | Shortest Word Distance | Easy | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LintCode_924_Shortest-Word-Distance.md) |
| 955 | Implement Queue by Circular Array | Medium | [Queue](https://github.com/chkao831/Algo_learning_notes/blob/main/Queue/LintCode_955_Implement-Queue-by-Circular-Array.md) |
| 1027 | Similar RGB Color | Easy | [Operator](https://github.com/chkao831/Algo_learning_notes/blob/main/Operator/LintCode_1017_Similar-RGB-Color.md) |
| 1032 | Letter Case Permutation | Easy | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_1032_Letter-Case-Permutation.md) |
| 1144 | Range Addition II | Easy | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_1144_Range-Addition-II.md) |
| 1179 | Friend Circles | Medium | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_1179_Friend-Circles.md) |
| 1226 | Minimum Moves to Equal Array Elements II | Medium | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_1226_Minimum-Moves-to-Equal-Array-Elements-II.md) |
| 1253 | Convert a Number to Hexadecimal | Easy | [Operator](https://github.com/chkao831/Algo_learning_notes/blob/main/Operator/LintCode_1253_Convert-a-Number-to-Hexadecimal.md) |
| 130 | Bash Game | Easy | [DP(math)](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LintCode_1300_Bash-Game.md) |
| 1359 | Convert Sorted Array to Binary Search Tree | Easy | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_1359_Convert-Sorted-Array-to-Binary-Search-Tree.md) |
| 1524 | Search in a Binary Search Tree | Easy | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_1524_Search-in-a-Binary-Search-Tree.md) |
| 1665 | Calculate number | Easy | [Operator](https://github.com/chkao831/Algo_learning_notes/blob/main/Operator/LintCode_1665_Calculate-number.md) |
| 1881 | Aircraft seat | Easy | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_1881_Aircraft-seat.md) |
| 1820 | Find Letter | Easy | [Operator](https://github.com/chkao831/Algo_learning_notes/blob/main/Operator/LintCode_1820_Find-Letter.md) |
| 2929 | Find the most expensive items | Naive | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_2929_Find-the-most-expensive-items.md) |

## Problems (chronologically ordered)
| Source |  Index  | Topic  |  Link | Difficulty | Timestamp |
|  ----  |  ----  | ----  | ----  | ----  | ----  | 
| Lint | 415 | Valid Palindrome | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_415_Valid-Palindrome.md) | Medium | 20220910 |
| Lint | 891 | Valid Palindrome II | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_891_Valid-Palindrome-II.md) | Medium |  |
| Leet | 1 | Two Sum | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_1_Two-Sum.md); <br/>[Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_1_Two-sum.md) | Easy |  |
| Leet | 454 | 4Sum II | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_454_4Sum-II.md) | Medium |  |
| Lint | 607 | Two Sum III - Data structure design | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_607_Two-Sum-III-Data-structure-design.md); <br/>[Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LintCode_607_Two-Sum-III-Data-structure-design.md) | Easy |  |
| Leet | 147 | Insertion Sort List | [LinkedList](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_147_Insertion-Sort-List.md) | Medium |  |
| Lint | 57 | 3Sum | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_57_3Sum.md) | Medium |  |
| Leet | 611 | Valid Triangle Number | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_611_Valid-Triangle-Number.md) | Medium |  |
| Lint | 609 | Two sum - Less than or equal to target | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_609_Two-Sum-Less-than-or-equal-to-target.md) | Medium |  |
| Leet | 259 | 3Sum Smaller | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_259_3Sum-Smaller.md) | Medium |  |
| Leet | 18 | 4Sum | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_18_4Sum.md) | Medium |  |
| Lint | 464 | Sort Integers II | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_464_Sort-Integers-II_QuickSort.md) | Easy |  |
| Lint | 31 | Partition Array | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_31_Partition-Array.md) | Medium |  | 
| Lint | 144 | Interleaving Positive and Negative Numbers | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_144_Interleaving-Positive-and-Negative-Numbers.md) | Medium |  |
| Lint | 373 | Partition Array by Odd and Even | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_373_Partition-Array-by-Odd-and-Even.md) | Medium |  |
| Lint | 49 | Sort Letters by Case | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_49_Sort-Letters-by-Case.md) | Medium |  |
| Lint | 148 | Sort Colors | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_148_Sort-Colors.md) | Medium |  |
| Lint | 143 | Sort Colors II | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_143_Sort-Colors-II.md) | Medium |  |
| Lint | 539 | Move Zeroes | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_539_move-zeroes.md) | Medium |  |
| Lint | 407 | Plus One | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_407_Plus-One.md) | Easy |  |
| Lint | 1665 | Calculate number | [Operator](https://github.com/chkao831/Algo_learning_notes/blob/main/Operator/LintCode_1665_Calculate-number.md) | Easy |  |
| Leet | 86 | Partition List | [LinkedList](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_86-Partition-List.md) | Medium |  |
| Leet | 2161 | Partition Array According to Given Pivot | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_2161_Partition-Array-According-to-Given-Pivot.md) | Medium |  |
| Leet | 922 | Sort Array By Parity II | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_922_Sort-Array-By-Parity-II.md) | Easy |  |
| Leet | 763 | Partition Labels | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_763_Partition-Labels.md) | Medium |  |
| Leet | 215 | Kth Largest Element in an Array | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LeetCode_215_Kth-Largest-Element-in-an-Array_QuickSelect.md) | Medium |  |
| Lint | 80 | Median | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_80_Median.md) | Medium |  |
| Lint | 65 | Median of two Sorted Arrays | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_65_Median-of-two-Sorted-Arrays.md) | Hard |  |
| Lint | 1226 | Minimum Moves to Equal Array Elements II | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_1226_Minimum-Moves-to-Equal-Array-Elements-II.md) | Medium |  |
| Lint | 625 | Partition Array II | [Two Pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_625_Partition-Array-II.md) | Medium |  |
| Lint | 479 | Second Max of Array | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_479_Second-Max-of-Array.md) | Easy | |
| Leet | 913 | Sort an Array | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LeetCode_913_Sort-an-Array.md) | Medium |  |
| Leet | 2031 | Count Subarrays With More Ones Than Zeros | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LeetCode_2031_Count-Subarrays-With-More-Ones-Than-Zeros.md) | Medium |  |
| Lint | 716 | Add and Search | [Two Pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_716_Add-and-Search.md);<br/>[Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LintCode_716_Add-and-Search.md) | Easy |  |
| Lint | 457 | Classical Binary Search | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_457_Classical-Binary-Search.md) | Easy |  |
| Lint | 458 | Last Position of Target | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_458_Last-Position-of-Target.md) | Easy |  | 
| Lint | 585 | Maximum Number in Mountain Sequence | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_585_Maximum-Number-in-Mountain-Sequence.md) | Medium |  |
| Lint | 75 | Find Peak Element | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_75_Find-Peak-Element.md) | Medium |  |
| Lint | 1144 | Range Addition II | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_1144_Range-Addition-II.md) | Easy |  |
| Lint | 447 | Search in a Big Sorted Array | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_447_Search-in-a-Big-Sorted-Array.md) | Medium |  |
| Lint | 460 | Find K Closest Elements | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_460_Find-K-Closest-Elements.md) | Medium |  |
| Leet | 658 | Find K Closest Elements | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LeetCode_658_Find-K-Closest-Elements.md) | Medium |  |
| Lint | 159 | Find Minimum in Rotated Sorted Array | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_159_Find-Minimum-in-Rotated-Sorted-Array.md) | Medium |  |
| Lint | 160 | Find Minimum in Rotated Sorted Array II | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_160_Find-Minimum-in-Rotated-Sorted-Array-II.md) | Medium |  |
| Lint | 62 | Search in Rotated Sorted Array | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_62_Search-in-Rotated-Sorted-Array.md) | Medium |  |
| Lint | 63 | Search in Rotated Sorted Array II | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_63_Search-in-Rotated-Sorted-Array-II.md) | Medium |  |
| Lint | 183 | Wood Cut | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_183_Wood-Cut.md) | Hard |  |
| Leet | 74 | Search a 2D Matrix | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LeetCode_74_Search-a-2D-Matrix.md) | Medium |  |
| Lint | 38 | Search a 2D Matrix II | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_38_Search-a-2D-Matrix-II.md) | Medium |  | 
| Lint | 600 | Smallest Rectangle Enclosing Black Pixels | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_600_Smallest-Rectangle-Enclosing-Black-Pixels.md) | Hard |  |
| Lint | 437 | Copy Books | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_437_Copy-Books.md) | Medium |  |
| Lint | 492 | Implement Queue by Linked List | [Queue](https://github.com/chkao831/Algo_learning_notes/blob/main/Queue/LintCode_492_Implement-Queue-by-Linked-List.md) | Easy |  |
| Lint | 493 | Implement Queue by Linked List II | [Queue](https://github.com/chkao831/Algo_learning_notes/blob/main/Queue/LintCode_493_Implement-Queue-by-Linked-List-II.md) | Easy |  |
| Lint | 955 | Implement Queue by Circular Array | [Queue](https://github.com/chkao831/Algo_learning_notes/blob/main/Queue/LintCode_955_Implement-Queue-by-Circular-Array.md) | Medium |  |
| Leet | 102 | Binary Tree Level Order Traversal | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LeetCode_102_Binary-Tree-Level-Order-Traversal.md) | Medium |  |
| Lint | 137 | Clone Graph | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_137_Clone-Graph.md) | Medium |  | 
| Lint | 120 | Word Ladder | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_120_Word-Ladder.md) | Hard |  | 
| Lint | 433 | Number of Islands | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_433_Number-of-Islands.md) | Easy |  |
| Lint | 611 | Knight Shortest Path | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_611_Knight-Shortest-Path.md) | Medium |  |
| Lint | 630 | Knight Shortest Path II | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_630_Knight-Shortest-Path-II.md) | Medium |  |
| Lint | 1179 | Friend Circles | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_1179_Friend-Circles.md) | Medium |  |
| Lint | 178 | Graph Valid Tree | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_178_Graph-Valid-Tree.md) | Medium |  |
| Lint | 618 | Search Graph Nodes | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_618_Search-Graph-Nodes.md) | Medium |  | 
| Lint | 431 | Connected Component in Undirected Graph | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_431_Connected-Component-in-Undirected-Graph.md) | Medium |  |
| Lint | 598 | Zombie in Matrix | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_598_Zombie-in-Matrix.md) | Medium |  |
| Lint | 573 | Build Post Office II | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_573_Build-Post-Office-II.md) | Hard |  | 
| Lint | 1881 | Aircraft seat | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_1881_Aircraft-seat.md) | Easy |  | 
| Lint | 792 | Kth Prime Number | [Operator](https://github.com/chkao831/Algo_learning_notes/blob/main/Operator/LintCode_792_Kth-Prime-Number.md) | Easy |  |
| Lint | 127 | Topological Sorting | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_127_Topological-Sorting.md) | Medium |  | 
| Lint | 615 | Course Schedule | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_615_Course-Schedule.md) | Medium |  | 
| Lint | 616 | Course Schedule II | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_616_Course-Schedule-II.md) | Medium |  |
| Lint | 605 | Sequence Reconstruction | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_605_Sequence-Reconstruction.md) | Medium |  |
| Lint | 892 | Alien Dictionary | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_892_Alien-Dictionary.md) | Hard |  |
| Lint | 17 | Subsets | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_17_Subsets.md#bfs); [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_17_Subsets.md#dfs); [Binary Operator](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_17_Subsets.md#binary-operator) | Medium |  |
| Lint | 7 | Serialize and Deserialize Binary Tree | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LintCode_7_Serialize-and-Deserialize-Binary-Tree.md) | Medium |  |
| Lint | 1820 | Find Letter | [Operator](https://github.com/chkao831/Algo_learning_notes/blob/main/Operator/LintCode_1820_Find-Letter.md) | Easy | 20221001 | 
| Lint | 1027 | Similar RGB Color | [Operator](https://github.com/chkao831/Algo_learning_notes/blob/main/Operator/LintCode_1017_Similar-RGB-Color.md) | Easy |  |
| Lint | 924 | Shortest Word Distance | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LintCode_924_Shortest-Word-Distance.md) | Easy | |
| Leet | 144 | Binary Tree Preorder Traversal | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_144_Binary-Tree-Preorder-Traversal.md) | Easy | |
| Leet | 94 | Binary Tree Inorder Traversal | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_94_Binary-Tree-Inorder-Traversal.md) | Easy | |
| Leet | 173 | Binary Search Tree Iterator | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_173_Binary-Search-Tree-Iterator.md) | Medium | |
| Lint | 95 | Validate Binary Search Tree | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_95_Validate-Binary-Search-Tree.md) | Medium | |
| Leet | 230 | Kth Smallest Element in a BST | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_230_Kth-Smallest-Element-in-a-BST.md) | Medium | |
| Leet | 270 | Closest Binary Search Tree Value I | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_270_Closest-Binary-Search-Tree-Value.md) | Medium | |
| Leet | 272 | Closest Binary Search Tree Value II | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_272_Closest-Binary-Search-Tree-Value-II.md) | Medium | |
| Lint | 1359 | Convert Sorted Array to Binary Search Tree | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_1359_Convert-Sorted-Array-to-Binary-Search-Tree.md) | Easy | | 
| Lint | 689 | Two Sum IV - Input is a BST | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_689_Two-Sum-IV-Input-is-a-BST.md) | Medium | | 
| Lint | 1524 | Search in a Binary Search Tree | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_1524_Search-in-a-Binary-Search-Tree.md) | Easy | |
| Lint | 11 | Search Range in Binary Search Tree  | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_11_Search-Range-in-Binary-Search-Tree.md) | Medium | |
| Lint | 85 | Insert Node in a Binary Search Tree | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_85_Insert-Node-in-a-Binary-Search-Tree.md) | Easy | |
| Lint | 701 | Trim a Binary Search Tree | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_701_Trim-a-Binary-Search-Tree.md) | Medium | | 
| Leet | 145 | Binary Tree Postorder Traversal | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_145_Binary-Tree-Postorder-Traversal.md) | Easy | |
| Leet | 257 | Binary Tree Paths | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_257_Binary-Tree-Paths.md) | Easy | |
| Leet | 110 | Balanced Binary Tree | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_110_Balanced-Binary-Tree.md)  | Easy | | 
| Leet | 104 | Maximum Depth of Binary Tree | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_104_Maximum-Depth-of-Binary-Tree.md) | Easy | | 
| Lint | 628 | Maximum Subtree | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_628_Maximum-Subtree.md) | Easy | |
| Lint | 596 | Minimum Subtree | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_596_Minimum-Subtree.md) | Easy | |
| Leet | 1120 | Maximum Average Subtree | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_1120_Maximum-Average-Subtree.md) | Medium | | 
| Lint | 88 | Lowest Common Ancestor of a Binary Tree | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_88_Lowest-Common-Ancestor-of-a-Binary-Tree.md) | Medium | | 
| Lint | 474 | Lowest Common Ancestor II | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_474_Lowest-Common-Ancestor-II.md) | Easy | |
| Lint | 578 | Lowest Common Ancestor III | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_578_Lowest-Common-Ancestor-III.md) | Medium | |
| Lint | 175 | Invert Binary Tree | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_175_Invert-Binary-Tree.md) | Easy | |
| Lint | 453 | Flatten Binary Tree to Linked List | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_453_Flatten-Binary-to-Linked-List.md) | Easy | |
| Lint | 18 | Subsets II | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_18_Subsets-II.md) | Medium | | 
| Lint | 425 | Letter Combinations of a Phone Number | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_425_Letter-Combinations-of-a-Phone-Number.md) | Medium | | 
| Lint | 90 | k Sum II | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_90_k-Sum-II.md) | Medium | |
| Lint | 135 | Combination Sum | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_135_Combination-Sum.md) | Medium | |
| Lint | 15 | Permutations | DFS ([Recursive](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_15_Permutations.md#dfs-recursive-approach)/[Iterative](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_15_Permutations.md#dfs-%E9%9D%9E%E9%81%9E%E6%AD%B8%E7%9A%84%E6%96%B9%E5%BC%8F%E5%AF%A6%E7%8F%BE%E6%8E%92%E5%88%97%E5%92%8C%E7%B5%84%E5%90%88%E9%A1%9Edfs)) | Medium | |
| Lint | 16 | Permutations II | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_16_Permutations-II.md) | Medium | |
| Lint | 10 | String Permutation II | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_10_String-Permutation-II.md) | Medium | |
| Lint | 816 | Traveling Salesman Problem (TSP) | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_816_Traveling-Salesman-Problem.md) | Hard | |
| Lint | 132 | Word Search II | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_132_Word-Search-II.md) | Hard | |
| Lint | 121 | Word Ladder II | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_121_Word-Ladder-II.md) | Hard | |
| Leet | 91 | Decode Ways | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_91_Decode-Ways.md) | Medium | |
| Leet | 51 | N-Queens | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_51_N-Queens.md) | Hard | |
| Lint | 802 | Sudoku Solver | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_802_Sudoku-Solver.md) | Hard | |
| Leet | 31 | Next Permutation | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_31_Next-Permutation.md) (Iterative) | Medium | |
| Lint | 197 | Permutation Index | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_197_Permutation-Index.md) (Iterative) | Medium | |
| Leet | 2449 | Minimum Number of Operations to Make Arrays Similar | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LeetCode_2449_Minimum-Number-of-Operations-to-Make-Arrays-Similar.md) | Hard | |
| Lint | 128 | Hash Function | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LintCode_128_Hash-Function.md) | Easy | 20221101 |
| Lint | 129 | Rehashing | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LintCode_129_Rehashing.md) | Medium | |
| Lint | 868 | Maximum Average Subarray | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_868_Maximum-Average-Subarray.md) | Easy | |
| Lint | 2929 | Find the most expensive items | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_2929_Find-the-most-expensive-items.md) | Naive | |
| Lint | 134 | LRU Cache | [LinkedList(Hash)](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LintCode_134_LRU-Cache.md) | Hard | |
| Leet | 380 | Insert Delete GetRandom O(1) | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_380_Insert-Delete-GetRandom-O(1).md) | Medium | |
| Lint | 685 | First Unique Number in Data Stream (offline algo) | [Queue](https://github.com/chkao831/Algo_learning_notes/blob/main/Queue/LintCode_685_First-Unique-Number-in-Data-Stream.md) | Medium | |  
| Leet | 1429 | First Unique Number (online algo) | [LinkedList](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_1429_First-Unique-Number.md) | Medium | |
| Lint | 130 | Heapify | [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LintCode_130_Heapify.md) | Medium | |
| Leet | 263 | Ugly Number | [Array](https://github.com/chkao831/Algo_learning_notes/blob/8b01966f0d4aaabc6c934cc202b0f403cacbac0e/Array/LeetCode_263_Ugly-Number.md) | Easy | |
| Leet | 264 | Ugly Number II | [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LeetCode_264_Ugly-Number-II.md) | Medium | |
| Lint | 612 | K Closest Points | [QuickSelect](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LintCode_612_K-Closest-Points.md#quick-select--sort-top-k--on--klogk); [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LintCode_612_K-Closest-Points.md#heap--onlogk) | Medium | 20221201 |
| Lint | 545 | Top k Largest Numbers II | [QuickSelect](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LintCode_545_Top-k-Largest-Numbers-II.md#quick-select--sort-top-k--on--klogk-topk-o1-add); [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LintCode_545_Top-k-Largest-Numbers-II.md#heap--onlogk-topk-ologn-add) | Medium | |
| Lint | 471 | Top K Frequent Words | [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LintCode_471_Top-K-Frequent-Words.md) | Medium | |
| Lint | 1253 | Convert a Number to Hexadecimal | [Operator](https://github.com/chkao831/Algo_learning_notes/blob/main/Operator/LintCode_1253_Convert-a-Number-to-Hexadecimal.md) | Easy | |
| Lint | 172 | Remove Element | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_172_Remove-Element.md) | Easy | |
| Leet | 451 | Sort Characters By Frequency | [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LeetCode_451_Sort-Characters-By-Frequency.md) | Medium | |
| Leet | 155 | Min Stack | [Stack](https://github.com/chkao831/Algo_learning_notes/blob/main/Stack/LeetCode_155_Min-Stack.md) | Medium | |
| Leet | 716 | Max Stack | [Stack](https://github.com/chkao831/Algo_learning_notes/blob/main/Stack/LeetCode_716_Max-Stack.md) | Hard | |
| Leet | 232 | Implement Queue using Stacks | [Stack](https://github.com/chkao831/Algo_learning_notes/blob/main/Stack/LeetCode_232_Implement-Queue-using-Stacks.md) | Medium | |
| Leet | 225 | Implement Stack using Queues | [Queue](https://github.com/chkao831/Algo_learning_notes/blob/main/Queue/LeetCode_225_Implement-Stack-using-Queues.md) | Easy | |
| Leet | 2256 | Minimum Average Difference | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LeetCode_2256_Minimum-Average-Difference.md) | Medium | |
| Lint | 6 | Merge Two Sorted Arrays | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_6_Merge-Two-Sorted-Arrays.md) | Easy | |
| Lint | 165 | Merge Two Sorted Lists | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_165_Merge-Two-Sorted-Lists.md) | Easy | |
| Lint | 104 | Merge K Sorted Lists | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_104_Merge-K-Sorted-Lists.md)<br/>(Heap/PairwiseMerge/MergeSort) | Medium | |
| Lint | 64 | Merge Sorted Array | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_64_Merge-Sorted-Array.md) | Easy | |
| Lint | 839 | Merge Two Sorted Interval Lists | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_839_Merge-Two-Sorted-Interval-Lists.md) | Easy | |
| Lint | 577 | Merge K Sorted Interval Lists | [ExternalSorting<br/>(Heap)](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_577_Merge-K-Sorted-Interval-Lists.md) | Medium | |
| Lint | 547 | Intersection of Two Arrays | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_547_Intersection-of-Two-Arrays.md)<br/>(TwoPointers/BinarySearch) | Easy | |
| Lint | 548 | Intersection of Two Arrays II | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_548_Intersection-of-Two-Arrays-II.md)<br/>(Hashmap/TwoPointers) | Easy | |
| Lint | 793 | Intersection of Arrays | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_793_Intersection-of-Arrays.md)<br/>(Hashmap/Heap) | Medium | |
| Lint | 654 | Sparse Matrix Multiplication | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LintCode_654_Sparse-Matrix-Multiplication.md) | Medium | | 
| Leet | 872 | Leaf-Similar Trees | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_872_Leaf-Similar-Trees.md) | Easy | |
| Leet | 328 | Odd Even Linked List | [LinkedList](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_328_Odd-Even-Linked-List.md) | Medium | |
| Lint | 13 | Implement strStr() | [Two Pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_13_Implement-strStr().md) | Naive | |
| Leet | 1026 | Maximum Difference Between Node and Ancestor | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_1026_Maximum-Difference-Between-Node-and-Ancestor.md) | Medium | |
| Leet | 1339 | Maximum Product of Splitted Binary Tree | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_1339_Maximum-Product-of-Splitted-Binary-Tree.md) | Medium | |
| Leet | 124 | Binary Tree Maximum Path Sum | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_124_Binary%20Tree-Maximum-Path-Sum.md) | Hard | |
| Leet | 70 | Climbing Stairs | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_70_Climbing-Stairs.md#dfs-brute-force)/[DP](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_70_Climbing-Stairs.md#dp) | Easy | |
| Leet | 931 | Minimum Falling Path Sum | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_931_Minimum-Falling-Path-Sum.md) | Medium | |
| Lint | 1032 | Letter Case Permutation | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LintCode_1032_Letter-Case-Permutation.md) | Easy | |
| Leet | 198 | House Robber | [DP](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LeetCode_198_House-Robber.md) | Medium | |
| Lint | 514 | Paint Fence | [DP](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LintCode_514_Paint-Fence.md) | Easy | |
| Leet | 1143 | Longest Common Subsequence | [DP](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LeetCode_1143_Longest-Common-Subsequence.md) | Medium | |
| Leet | 150 | Evaluate Reverse Polish Notation | [Stack](https://github.com/chkao831/Algo_learning_notes/blob/main/Stack/LeetCode_150_Evaluate-Reverse-Polish-Notation.md) | Medium | |
| Leet | 739 | Daily Temperatures | [Stack](https://github.com/chkao831/Algo_learning_notes/blob/main/Stack/LeetCode_739_Daily-Temperatures.md) | Medium | |
| Leet | 841 | Keys and Rooms | [Stack](https://github.com/chkao831/Algo_learning_notes/blob/main/Stack/LeetCode_841_Keys-and-Rooms.md) | Medium | |
| Leet | 886 | Possible Bipartition | [BFS](https://github.com/chkao831/Algo_learning_notes/blob/main/BFS/LeetCode_886_Possible-Bipartition.md) | Medium | |
| Leet | 834 | Sum of Distances in Tree | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_834_Sum-of-Distances-in-Tree.md) | Hard | |
| Leet | 121 | Best Time to Buy and Sell Stock | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LeetCode_121_Best-Time-to-Buy-and-Sell-Stock.md) | Easy | |
| Leet | 122 | Best Time to Buy and Sell Stock II | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LeetCode_122_Best-Time-to-Buy-and-Sell-Stock-II.md) | Medium | |
| Leet | 309 | Best Time to Buy and Sell Stock with Cooldown | [DP](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LeetCode_309_Best-Time-to-Buy-and-Sell-Stock-with-Cooldown.md) | Medium | |
| Leet | 790 | Domino and Tromino Tiling | [DP](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LeetCode_790_Domino-and-Tromino-Tiling.md) | Medium | |
| Leet | 2389 | Longest Subsequence With Limited Sum | [BinarySearch](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LeetCode_2389_Longest-Subsequence-With-Limited-Sum.md) | Easy | |
| Leet | 55 | Jump Game | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_55_Jump-Game.md) | Medium | |
| Leet | 120 | Triangle | [DFS/DP](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LeetCode_120_Triangle.md) | Medium | |
| Lint | 1300 | Bash Game | [DP(math)](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LintCode_1300_Bash-Game.md) | Easy | |
| Leet | 2279 | Maximum Bags With Full Capacity of Rocks | [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LeetCode_2279_Maximum-Bags-With-Full-Capacity-of-Rocks.md) | Medium | |  
| Leet | 1962 | Remove Stones to Minimize the Total | [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LeetCode_1962_Remove-Stones-to-Minimize-the-Total.md) | Medium | |
| Leet | 1834 | Single-Threaded CPU | [Heap](https://github.com/chkao831/Algo_learning_notes/blob/main/Heap/LeetCode_1834_Single-Threaded-CPU.md) | Medium | |
| Leet | 980 | Unique Paths III | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_980_Unique-Paths-III.md) | Hard | |
| Leet | 290 | Word Pattern | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_290_Word-Pattern.md) | Easy | 202301 |
| Leet | 62 | Unique Path | [DP](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LeetCode_62_Unique-Paths.md) | Medium | |
| Leet | 2244 | Minimum Rounds to Complete All Tasks | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_2244_Minimum-Rounds-to-Complete-All-Tasks.md) | Medium | |
| Leet | 452 | Minimum Number of Arrows to Burst Balloons | [ExternalSorting](https://github.com/chkao831/Algo_learning_notes/blob/main/ExternalSorting/LeetCode_452_Minimum-Number-of-Arrows-to-Burst-Balloons.md) | Medium | |
| Leet | 134 | Gas Station | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LeetCode_134_Gas-Station.md) | Medium | |
| Leet | 149 | Max Points on a Line | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_149_Max-Points-on-a-Line.md) | Hard | |
| Leet | 100 | Same Tree | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_100_Same-Tree.md) | Easy | |
| Lint | 101 | Remove Duplicates from Sorted Array II | [Two Pointer](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_101_Remove-Duplicates-from-Sorted-Array-II.md) | Easy | |
| Leet | 1443 | Minimum Time to Collect All Apples in a Tree | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_1443_Minimum-Time-to-Collect-All-Apples-in-a-Tree.md) | Medium | |
| Leet | 1519 | Number of Nodes in the Sub-Tree With the Same Label | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_1519_Number-of-Nodes-in-the-Sub-Tree-With-the-Same-Label.md) | Medium | |
| Leet | 2246 | Longest Path With Different Adjacent Characters | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_2246_Longest-Path-With-Different-Adjacent-Characters.md) | Hard | |
| Leet | 1061 | Lexicographically Smallest Equivalent String | [DFS](https://github.com/chkao831/Algo_learning_notes/blob/main/DFS/LeetCode_1061_Lexicographically-Smallest-Equivalent-String.md) | Medium | |
| Leet | 1626 | Best Team With No Conflicts | [DP](https://github.com/chkao831/Algo_learning_notes/blob/main/DP/LeetCode_1626_Best-Team-With-No-Conflicts.md) | Medium | | 
| Leet | 1071 | Greatest Common Divisor of Strings | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LeetCode_1071_Greatest-Common-Divisor-of-Strings.md) | Easy | 202302 |
| Leet | 953 |  Verifying an Alien Dictionary | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_953_Verifying-an-Alien-Dictionary.md) | Easy | |

(^: Attempted; partially solved)
