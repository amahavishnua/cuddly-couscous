'''
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
'''

class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)

'''

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            if target-i in nums[nums.index(i)+1:]:
                return [nums.index(i),nums[nums.index(i)+1:].index(target-i)+nums.index(i)+1]
            
            elif i-target in nums[nums.index(i)+1:]:
                return [nums.index(i),nums[nums.index(i)+1:].index(i-target)+nums.index(i)+1]
        

'''
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.



'''

class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            x=int('-'+str(x)[::-1][:-1])
        else:
            x=int(str(x)[::-1])
        if x < -2**31 or x >2**31-1:
            return 0
        return int(str(x))


'''
Input: s = "III"
Output: 3
Example 2:

Input: s = "IV"
Output: 4
Example 3:

Input: s = "IX"
Output: 9
Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

'''


values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            # 
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            # 
            else:
                total += values[s[i]]
                i += 1
        return total