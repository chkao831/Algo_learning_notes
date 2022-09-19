# Algorithm Learning Notes
> Since Sep 10, 2022\
> Last Updated on Sep 18, 2022

## Language
Python3

## Categories
#### Algorithms
- [Two pointers（雙指針）](https://github.com/chkao831/Algo_learning_notes/tree/main/Two-pointers)
- [Divide-and-Conquer（DnC, 分治）](https://github.com/chkao831/Algo_learning_notes/tree/main/DnC)
- [Binary Search（二分法）](https://github.com/chkao831/Algo_learning_notes/tree/main/BinarySearch)
- Sorting（排序）
  | Type | Average Time | Space | Algorithm Demo | Application | 
  |  ----  | ----  | ----  | ----  | ----  | 
  | Insertion Sort | O(n^2) | O(1) | [Leet147](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_147_Insertion-Sort-List.md) | 1. [[Lint607](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_607_Two-Sum-III-Data-structure-design.md)] Add number with Insertion Sort to the last, then swap to front with O(n) time. |
  | Quick Sort | O(nlogn) | O(logn) | [Lint464](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_464_Sort-Integers-II_QuickSort.md) | 1. [[Lint31](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_31_Partition-Array.md)] Partition highly resembles Quick Sort, except that the left-right partition is strict.<br/>2. [[Lint143](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_143_Sort-Colors-II.md)] Recursion highly resembles Quick Sort, while the pivot (middle color) partition is strict.|
  | Quick Select | O(n) | O(1) | [Leet215](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LeetCode_215_Kth-Largest-Element-in-an-Array_QuickSelect.md) | Quick Select highly resembles [Quick Sort](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_464_Sort-Integers-II_QuickSort.md), except that one knows which part to search for the subsequent recursive call, so the time complexity reduces to O(n). |
  | Merge Sort | O(nlogn) | O(n) | [Leet913](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LeetCode_913_Sort-an-Array.md) | |
  
 #### Data Structures
- [Hashmap (哈希表)](https://github.com/chkao831/Algo_learning_notes/tree/main/Hashmap)
- [Array (數組)](https://github.com/chkao831/Algo_learning_notes/tree/main/Array)
- [Linked List (鏈表)](https://github.com/chkao831/Algo_learning_notes/tree/main/LinkedList)

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
| 86 | Partition List | Medium | [LinkedList](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_86-Partition-List.md) | 
| 147 | Insertion Sort List | Medium | [LinkedList](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_147_Insertion-Sort-List.md) |
| 215 | Kth Largest Element in an Array | Medium | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LeetCode_215_Kth-Largest-Element-in-an-Array_QuickSelect.md)|
| 259 | 3Sum Smaller | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_259_3Sum-Smaller.md)|
| 454 | 4Sum II | Medium | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_454_4Sum-II.md)|
| 611 | Valid Triangle Number | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_611_Valid-Triangle-Number.md)|
| 658 | Find K Closest Elements | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LeetCode_658_Find-K-Closest-Elements.md) | 
| 763 | Partition Lables | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_763_Partition-Labels.md) |
| 913 | Sort an Array | Medium | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LeetCode_913_Sort-an-Array.md) |
| 922 | Sort Array By Parity II | Easy | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_922_Sort-Array-By-Parity-II.md) |
| 2161 | Partition Array According to Given Pivot | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_2161_Partition-Array-According-to-Given-Pivot.md) |
| 2031 | Count Subarrays With More Ones Than Zeros | Medium | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LeetCode_2031_Count-Subarrays-With-More-Ones-Than-Zeros.md) |

#### LintCode
| Index | Topic | Difficulty | Link(s) |
|  ----  | ----  | ----  | ----  |
| 31 | Partition Array | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_31_Partition-Array.md) |
| 49 | Sort Letters by Case | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/tree/main/Two-pointers) |
| 57 | 3Sum | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_57_3Sum.md) |
| 62 | Search in Rotated Sorted Array | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_62_Search-in-Rotated-Sorted-Array.md) |
| 63 | Search in Rotated Sorted Array II | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_63_Search-in-Rotated-Sorted-Array-II.md) |
| 65 | Median of two Sorted Arrays | Hard | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_65_Median-of-two-Sorted-Arrays.md) |
| 75 | Find Peak Element | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_75_Find-Peak-Element.md) |
| 80 | Median | Medium | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_80_Median.md) |
| 143 | Sort Colors II | Medium | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_143_Sort-Colors-II.md) | 
| 144 | Interleaving Positive and Negative Numbers | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_144_Interleaving-Positive-and-Negative-Numbers.md) |
| 148 | Sort Colors | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_148_Sort-Colors.md) | 
| 159 | Find Minimum in Rotated Sorted Array | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_159_Find-Minimum-in-Rotated-Sorted-Array.md) |
| 160 | Find Minimum in Rotated Sorted Array II | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_160_Find-Minimum-in-Rotated-Sorted-Array-II.md) |
| 183 | Wood Cut | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_183_Wood-Cut.md) |
| 373* | Partition Array by Odd and Even | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_373_Partition-Array-by-Odd-and-Even.md) |
| 407 | Plus One | Easy | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_407_Plus-One.md) |
| 415 | Valid Palindrome | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_415_Valid-Palindrome.md) |
| 447 | Search in a Big Sorted Array | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_447_Search-in-a-Big-Sorted-Array.md) |
| 457 | Classical Binary Search | Easy | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_457_Classical-Binary-Search.md) |
| 458 | Last Position of Target | Easy | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_458_Last-Position-of-Target.md) | 
| 460 | Find K Closest Elements | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_460_Find-K-Closest-Elements.md) | 
| 464 | Sort Integers II | Easy | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_464_Sort-Integers-II_QuickSort.md) 
| 479 | Second Max of Array | Easy | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_479_Second-Max-of-Array.md) |
| 539 | Move Zeroes | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_539_move-zeroes.md) | 
| 585 | Maximum Number in Mountain Sequence | Medium | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_585_Maximum-Number-in-Mountain-Sequence.md) |
| 607 | Two Sum III - Data structure design | Easy | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_607_Two-Sum-III-Data-structure-design.md); <br/>[Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LintCode_607_Two-Sum-III-Data-structure-design.md) |
| 609* | Two sum - Less than or equal to target | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_609_Two-Sum-Less-than-or-equal-to-target.md) |
| 625 | Partition Array II | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_625_Partition-Array-II.md) |
| 716 | Add and Search | Easy | [Two Pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_716_Add-and-Search.md);<br/>[Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LintCode_716_Add-and-Search.md) |
| 891 | Valid Palindrome II | Medium | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_891_Valid-Palindrome-II.md) |
| 1144 | Range Addition II | Easy | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_1144_Range-Addition-II.md) |
| 1226 | Minimum Moves to Equal Array Elements II | Medium | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_1226_Minimum-Moves-to-Equal-Array-Elements-II.md) |
| 1665 | Calculate number | Easy | [Operator](https://github.com/chkao831/Algo_learning_notes/blob/main/Operator/LintCode_1665_Calculate-number.md) |

## Problems (chronologically ordered)
| Source |  Index  | Topic  |  Link | Difficulty | Submission Date |
|  ----  |  ----  | ----  | ----  | ----  | ----  | 
| Lint | 415 | Valid Palindrome | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_415_Valid-Palindrome.md) | Medium | 20220910 |
| Lint | 891 | Valid Palindrome II | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_891_Valid-Palindrome-II.md) | Medium | 20220910 |
| Leet | 1 | Two Sum | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_1_Two-Sum.md); <br/>[Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_1_Two-sum.md) | Easy | 20220910 |
| Leet | 454 | 4Sum II | [Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LeetCode_454_4Sum-II.md) | Medium | 20220910 |
| Lint | 607 | Two Sum III - Data structure design | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_607_Two-Sum-III-Data-structure-design.md); <br/>[Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LintCode_607_Two-Sum-III-Data-structure-design.md) | Easy | 20220910 |
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
| Lint | 1665 | Calculate number | [Operator](https://github.com/chkao831/Algo_learning_notes/blob/main/Operator/LintCode_1665_Calculate-number.md) | Easy | 20220913 |
| Leet | 86 | Partition List | [LinkedList](https://github.com/chkao831/Algo_learning_notes/blob/main/LinkedList/LeetCode_86-Partition-List.md) | Medium | 20220913 |
| Leet | 2161 | Partition Array According to Given Pivot | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_2161_Partition-Array-According-to-Given-Pivot.md) | Medium | 20220913 |
| Leet | 922 | Sort Array By Parity II | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_922_Sort-Array-By-Parity-II.md) | Easy | 20220913 |
| Leet | 763 | Partition Labels | [Two pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LeetCode_763_Partition-Labels.md) | Medium | 20220913 |
| Leet | 215 | Kth Largest Element in an Array | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LeetCode_215_Kth-Largest-Element-in-an-Array_QuickSelect.md) | Medium | 20220913 |
| Lint | 80 | Median | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_80_Median.md) | Medium | 20220913 |
| Lint | 65 | Median of two Sorted Arrays | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_65_Median-of-two-Sorted-Arrays.md) | Hard | 20220913 |
| Lint | 1226 | Minimum Moves to Equal Array Elements II | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LintCode_1226_Minimum-Moves-to-Equal-Array-Elements-II.md) | Medium | 20220914 |
| Lint | 625 | Partition Array II | [Two Pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_625_Partition-Array-II.md) | Medium | 20220914 |
| Lint | 479 | Second Max of Array | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_479_Second-Max-of-Array.md) | Easy | 20220915 |
| Leet | 913 | Sort an Array | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LeetCode_913_Sort-an-Array.md) | Medium | 20220915 |
| Leet | 2031 | Count Subarrays With More Ones Than Zeros | [DnC](https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LeetCode_2031_Count-Subarrays-With-More-Ones-Than-Zeros.md) | Medium | 20220915 |
| Lint | 716 | Add and Search | [Two Pointers](https://github.com/chkao831/Algo_learning_notes/blob/main/Two-pointers/LintCode_716_Add-and-Search.md);<br/>[Hashmap](https://github.com/chkao831/Algo_learning_notes/blob/main/Hashmap/LintCode_716_Add-and-Search.md) | Easy | 20220916 |
| Lint | 457 | Classical Binary Search | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_457_Classical-Binary-Search.md) | Easy | 20220916 |
| Lint | 458 | Last Position of Target | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_458_Last-Position-of-Target.md) | Easy | 20220916 | 
| Lint | 585 | Maximum Number in Mountain Sequence | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_585_Maximum-Number-in-Mountain-Sequence.md) | Medium | 20220916 |
| Lint | 75 | Find Peak Element | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_75_Find-Peak-Element.md) | Medium | 20220916 |
| Lint | 1144 | Range Addition II | [Array](https://github.com/chkao831/Algo_learning_notes/blob/main/Array/LintCode_1144_Range-Addition-II.md) | Easy | 20220917 |
| Lint | 447 | Search in a Big Sorted Array | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_447_Search-in-a-Big-Sorted-Array.md) | Medium | 20220917 |
| Lint | 460 | Find K Closest Elements | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_460_Find-K-Closest-Elements.md) | Medium | 20220917 |
| Leet | 658 | Find K Closest Elements | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LeetCode_658_Find-K-Closest-Elements.md) | Medium | 20220917 |
| Lint | 159 | Find Minimum in Rotated Sorted Array | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_159_Find-Minimum-in-Rotated-Sorted-Array.md) | Medium | 20220918 |
| Lint | 160 | Find Minimum in Rotated Sorted Array II | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_160_Find-Minimum-in-Rotated-Sorted-Array-II.md) | Medium | 20220918 |
| Lint | 62 | Search in Rotated Sorted Array | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_62_Search-in-Rotated-Sorted-Array.md) | Medium | 20220918 |
| Lint | 63 | Search in Rotated Sorted Array II | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_63_Search-in-Rotated-Sorted-Array-II.md) | Medium | 20220918 |
| Lint | 183 | Wood Cut | [Binary Search](https://github.com/chkao831/Algo_learning_notes/blob/main/BinarySearch/LintCode_183_Wood-Cut.md) | Hard | 20220918 |

(*: LintCode VIP only)\
(^: Attempted; partially resolved)

Leet74
