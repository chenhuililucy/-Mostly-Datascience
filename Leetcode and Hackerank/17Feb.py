#https://www.jianshu.com/p/6462ad3f2708

"""

Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

思路
和14题3Sum类似，由找到所有和为0的3个值，变为找到所有和离target最近的3个值。首先将数组按升序nums排序，再从左到右遍历。取一个值a作为基准值，再从数组中在a右边的值里选出两个值b, c，使得|target-a-b-c|最小。
解法

作者：小新_XX
链接：https://www.jianshu.com/p/6462ad3f2708
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def twoSumClosest(nums, c=0):
            '''
            从数组nums中找到组合(a, b),使得 |a + b - c|最小.
            返回值：满足条件的a, b之和: a*+b*
            '''
            i = 0
            j = len(nums)-1
            result = nums[i]+nums[j]
            while i < j:
                s = nums[i]+nums[j]
                if s == c:
                    return s    
                if abs(c-s)<abs(c-result):
                    result = s
                if s > c:
                    j -= 1
                elif s < c:
                    i += 1
            return result

        if len(nums) < 3:
            return None
        nums = sorted(nums) # 首先将nums排序
        for i in range(len(nums)-2):
            if i >= 1 and nums[i] == nums[i-1]: #跳过重复的a
                continue
            bc = twoSumClosest(nums[i+1:], target-nums[i]) #bc为满足条件的b,c之和
            if target == nums[i]+bc: #如果a+b+c和target相等，直接返回target
                return target
            if i == 0: #i = 0时，赋result初值
                result = nums[i]+bc
            else:#当前的a+b+c比前一个a+b+c更加接近target时，更新result
                if abs(target-nums[i]-bc)<abs(target - result):
                    result = nums[i] + bc 
        return result


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, c=0):
            '''
            从数组nums中找到所有的组合(a, b),使得 a + b = c.
            返回值：所有的和为-c的组合[[a1, b1, -c],[a2, b2, -c],..., [an, bn, -c]]
            '''
            result = []
            i = 0
            j = len(nums)-1
            while i < j:
                s = nums[i]+nums[j]
                if s == c:
                    if [nums[i], nums[j], -c] not in result: #结果不能包含重复值
                        result.append([nums[i], nums[j], -c])
                    i += 1
                    j -= 1
                elif s >c:
                    j -= 1
                else:
                    i += 1
            return result
        
        result = []
        if len(nums) < 3:
            return result
        nums = sorted(nums) # 首先将nums排序
        for i in range(len(nums)):
            if nums[i]>0: #nums[i]即为c. 由于数组从小到大排序，当c>0时三者之和不可能为0
                break
            if i >= 1 and nums[i] == nums[i-1]:#跳过重复的c
                continue
            r = twoSum(nums[i+1:], -nums[i])
            result += r
           
        return result
        

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num//1000]+C[num%1000//100]+X[num%100//10]+I[num%10]