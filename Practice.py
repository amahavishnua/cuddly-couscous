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

//
If sorted then


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums)-1
        while True:
            sums = nums[lo] + nums[hi]
            if sums < target:
                lo += 1
            elif sums > target:
                hi -= 1
            else:
                return [lo+1, hi+1]
        




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



        '''
#CYCLE FORMATION
        Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.


'''
class Solution:
    def isHappy(self, n: int) -> bool:
        check=[]
        while(len(str(n))>0):
            n=str(n)
            
            if len(n)==1 and n=='1':
                return True
            
            else:
                summ=0
                t=n
                for i in t:
                    summ=int(i)*int(i)+summ
                n=summ
                #checking cycle formed or not
                if int(n) in check:
                    return False
                check.append(summ)


'''
#BOATS problem Python LEETCODE 881
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lp=0
        rp=len(people)-1
        count=0
        while(lp<=rp):
            if lp==rp and people[lp]<=limit:
                print('executing')
                count+=1
            elif people[lp]+people[rp]<=limit:
                count=count+1
                lp=lp+1
            elif people[lp]+people[rp]>limit :
                if people[rp]<=limit :
                    count=count+1
            rp=rp-1
        return count



LinkedLists:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        strl1=''
        strl2=''
        print(l1)
        while(l1.val!=0):
            print(l1.val)
            strl1+=str(l1.val)
            if l1.next==None:
                break
            l1=l1.next
        print(strl1)
        while(l2.val!=0):
            print(l2.val)
            strl2+=str(l2.val)
            if l2.next==None:
                break
            l2=l2.next
        print(strl2)
        print(strl1,strl2)
        summ=str(int(strl1[::-1])+int(strl2[::-1]))[::-1]
        summLN=ListNode()
        tempa=ListNode(1)
        print(summ)
        summLN.val=summ[0]
        summLN.next=ListNode(summ[1])
        summLN.next.next=ListNode(summ[2])
        temp=ListNode(9)
        for i in range(0,5):
            temp=ListNode(i)
            temp=temp.next
        print(summLN)
        print(temp)
        return summLN
        