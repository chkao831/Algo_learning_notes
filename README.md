# Algorithm Learning Notes
> Since Sep 10, 2022\
> Last Updated on Sep 13, 2022

## Language
Python3

## Categories
#### Algorithms
- [Two pointers（雙指針）](https://github.com/chkao831/Algo_learning_notes/tree/main/Two-pointers)
- [Divide-and-Conquer（DnC, 分治）](https://github.com/chkao831/Algo_learning_notes/tree/main/DnC)
- Sorting（排序）
  | Type | Average Time | Space | Algorithm Demo | Application | 
  |  ----  | ----  | ----  | ----  | ----  | 
  | Insertion Sort | O(n^2) | O(1) | [Leet147](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_147_Insertion-Sort-List.md) | 1. [[Lint607](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_607_Two-Sum-III-Data-structure-design.md)] Add number with Insertion Sort to the last, then swap to front with O(n) time. |
  | Quick Sort | O(nlogn) | O(logn) | [Lint464](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_464_Sort-Integers-II_QuickSort.md) | 1. [[Lint31](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_31_Partition-Array.md)] Partition highly resembles Quick Sort, except that the left-right partition is strict.<br/>2. [[Lint143]](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_143_Sort-Colors-II.md) Recursion highly resembles Quick Sort, while the pivot (middle color) partition is strict.|
  
 #### Data Structures
- [Hashmap (哈希表)](https://github.com/chkao831/Algo_learning_notes/tree/main/Hashmap)
- [Array (數組)](https://github.com/chkao831/Algo_learning_notes/tree/main/Array)
- [Linked List (鏈表)](https://github.com/chkao831/Algo_learning_notes/tree/main/LinkedList)

## Problems (indexed)
#### LeetCode
| Index | Topic | Difficulty | Link(s) |
|  ----  | ----  | ----  | ----  |
| 1 | Two Sum | Easy | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_1_Two-Sum.md); [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_1_Two-sum.md)|
| 18 | 4Sum | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_18_4Sum.md)|
| 86 | Partition List | Medium | [LinkedList](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_86-Partition-List.md) | 
| 147 | Insertion Sort List | Medium | [LinkedList](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_147_Insertion-Sort-List.md) |
| 259 | 3Sum Smaller | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_259_3Sum-Smaller.md)|
| 454 | 4Sum II | Medium | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_454_4Sum-II.md)|
| 611 | Valid Triangle Number | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_611_Valid-Triangle-Number.md)|
| 763 | Partition Lables | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_763_Partition-Labels.md) |
| 922 | Sort Array By Parity II | Easy | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_922_Sort-Array-By-Parity-II.md) |
| 2161 | Partition Array According to Given Pivot | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_2161_Partition-Array-According-to-Given-Pivot.md) |

#### LintCode
| Index | Topic | Difficulty | Link(s) |
|  ----  | ----  | ----  | ----  |
| 31 | Partition Array | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_31_Partition-Array.md) |
| 49 | Sort Letters by Case | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/tree/main/Two-pointers) |
| 57 | 3Sum | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_57_3Sum.md) |
| 143 | Sort Colors II | Medium | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_143_Sort-Colors-II.md) | 
| 144 | Interleaving Positive and Negative Numbers | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_144_Interleaving-Positive-and-Negative-Numbers.md) |
| 148 | Sort Colors | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_148_Sort-Colors.md) | 
| 373* | Partition Array by Odd and Even | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_373_Partition-Array-by-Odd-and-Even.md) |
| 407 | Plus One | Easy | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_407_Plus-One.md) |
| 415 | Valid Palindrome | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_415_Valid-Palindrome.md) |
| 464 | Sort Integers II | Easy | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_464_Sort-Integers-II_QuickSort.md) 
| 539 | Move Zeroes | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_539_move-zeroes.md) | 
| 607 | Two Sum III - Data structure design | Easy | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_607_Two-Sum-III-Data-structure-design.md); [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LintCode_607_Two-Sum-III-Data-structure-design.md) |
| 609* | Two sum - Less than or equal to target | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_609_Two-Sum-Less-than-or-equal-to-target.md) |
| 891 | Valid Palindrome II | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_891_Valid-Palindrome-II.md) |

(*: LintCode VIP only)

## Problems (chronologically ordered)
| Source |  Index  | Topic  |  Link | Difficulty | Submission Date |
|  ----  |  ----  | ----  | ----  | ----  | ----  | 
| Lint | 415 | Valid Palindrome | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_415_Valid-Palindrome.md) | Medium | 20220910 |
| Lint | 891 | Valid Palindrome II | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_891_Valid-Palindrome-II.md) | Medium | 20220910 |
| Leet | 1 | Two Sum | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_1_Two-Sum.md) | Easy | 20220910 |
| Leet | 1 | Two Sum | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_1_Two-sum.md) | Easy | 20220910 |
| Leet | 454 | 4Sum II | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_454_4Sum-II.md) | Medium | 20220910 |
| Lint | 607 | Two Sum III - Data structure design | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_607_Two-Sum-III-Data-structure-design.md) | Easy | 20220910 |
| Lint | 607 | Two Sum III - Data structure design | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LintCode_607_Two-Sum-III-Data-structure-design.md) | Easy | 20220910 |
| Leet | 147 | Insertion Sort List | [LinkedList](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_147_Insertion-Sort-List.md) | Medium | 20220911 |
| Lint | 57 | 3Sum | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_57_3Sum.md) | Medium | 20220911 |
| Leet | 611 | Valid Triangle Number | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_611_Valid-Triangle-Number.md) | Medium | 20220911 |
| Lint | 609* | Two sum - Less than or equal to target | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_609_Two-Sum-Less-than-or-equal-to-target.md) | Medium | 20220911 |
| Leet | 259 | 3Sum Smaller | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_259_3Sum-Smaller.md) | Medium | 20220911 |
| Leet | 18 | 4Sum | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_18_4Sum.md) | Medium | 20220911 |
| Lint | 464 | Sort Integers II | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_464_Sort-Integers-II_QuickSort.md) | Easy | 20220912 |
| Lint | 31 | Partition Array | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_31_Partition-Array.md) | Medium | 20220912 | 
| Lint | 144 | Interleaving Positive and Negative Numbers | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_144_Interleaving-Positive-and-Negative-Numbers.md) | Medium | 20220912 |
| Lint | 373* | Partition Array by Odd and Even | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_373_Partition-Array-by-Odd-and-Even.md) | Medium | 20220912 |
| Lint | 49 | Sort Letters by Case | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_49_Sort-Letters-by-Case.md) | Medium | 20220912 |
| Lint | 148 | Sort Colors | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_148_Sort-Colors.md) | Medium | 20220912 |
| Lint | 143 | Sort Colors II | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_143_Sort-Colors-II.md) | Medium | 20220912 |
| Lint | 539 | Move Zeroes | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_539_move-zeroes.md) | Medium | 20220912 |
| Lint | 407 | Plus One | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_407_Plus-One.md) | Easy | 20220912 |
| Leet | 86 | Partition List | [LinkedList](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_86-Partition-List.md) | Medium | 20220913 |
| Leet | 2161 | Partition Array According to Given Pivot | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_2161_Partition-Array-According-to-Given-Pivot.md) | Medium | 20220913 |
| Leet | 922 | Sort Array By Parity II | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_922_Sort-Array-By-Parity-II.md) | Easy | 20220913 |
| Leet | 763 | Partition Labels | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_763_Partition-Labels.md) | Medium | 20220913 |
