### Count Subarrays With More Ones Than Zeros
https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/
>You are given a binary array nums containing only the integers 0 and 1. Return the number of subarrays in nums that have more 1's than 0's. Since the answer may be very large, return it modulo 10^9 + 7.
>
>A subarray is a contiguous sequence of elements within an array.
```python
MOD = 1000000007

class Solution:
    
    def __init__(self):

        self.prefixSum = []
        self.res = 0
        
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        if not nums: return
        
        self.prefixSum = [0]*len(nums)
        
        # Initialization
        for i in range(len(nums)):
            # (1) convert [0, 1] array to [-1, 1] array
            if nums[i] == 0:
                nums[i] = -1
            # (2) set elements for prefixSum
            if i == 0: # set first
                self.prefixSum[i] = nums[i]
            else: # second and so on
                self.prefixSum[i] = self.prefixSum[i-1]+nums[i]
            # (3) add prefixSum[0, index] as a solution, where prefixSum[index]>0
            if self.prefixSum[i] > 0:
                self.res += 1
        
        self.mergeSort(start=0, end=len(nums)-1)
        
        return (self.res % MOD)
    
    def mergeSort(self, start: int, end: int):
        # base
        if start >= end:
            return
        # recursive
        middle = (start+end)//2
        self.mergeSort(start=start, end=middle)
        self.mergeSort(start=middle+1, end=end)
        self.merge(start=start, end=end)
        
    def merge(self, start: int, end: int):
        
        temp = [0]*(end-start+1)
        index = 0
        
        middle = (start+end)//2
        left, right = start, middle+1
        while left <= middle and right <= end:
            """
            prefixSum切左右兩半，每個prefixSum的值implies an array, which sums from nums[0] to nums[i] (after transition)
            想要確認右邊目前指向的項, 究竟能跟左邊目前的項（及其左）做多少搭配（組成幾種砍法）。條件：右邊該prefixSum值>左邊。
                  L              R
                  v              v
            | 0 | 1 | ...| vs. | 2 | ...|
                <       add        >
            <         add          >
            """
            if self.prefixSum[left] < self.prefixSum[right]:
                temp[index] = self.prefixSum[left]
                left, index = left+1, index+1
            else:
                self.res += (left - start)
                temp[index] = self.prefixSum[right]
                right, index = right+1, index+1
        while left <= middle:
            temp[index] = self.prefixSum[left]
            left, index = left+1, index+1
        # 左邊已經全部加進去了（都小於右邊的值）(guaranteed prefixSum[left_part_last_element] < prefixSum[right])
        # 把右邊的項跟左邊做搭配
        while right <= end:
            self.res += (left - start) # prefixSum[left_part_last_element] < prefixSum[right]
            temp[index] = self.prefixSum[right]
            right, index = right+1, index+1
            
        for i in range(start, end+1):
            self.prefixSum[i] = temp[i-start]
```
#### Remark:
- prefixSum Diagram for reference: https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/discuss/1729813/Most-understandable-answer-with-diagram-(Java)
- Merge Sort: https://github.com/chkao831/Algo_learning_notes/blob/main/DnC/LeetCode_913_Sort-an-Array.md
- java version: https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/discuss/1522160/Java-merge-sort
#### Submission:
```
```
#### Complexity:
- Time: O(nlogn)
- Space: O(n)
