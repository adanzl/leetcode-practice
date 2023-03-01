"""
 * 给你一个正整数数组 nums ，请你返回一个数组 answer ，你需要将 nums 中每个整数进行数位分割后，按照 nums 中出现的 相同顺序 放入答案数组中。
 * 对一个整数进行数位分割，指的是将整数各个数位按原本出现的顺序排列成数组。
 * 比方说，整数 10921 ，分割它的各个数位得到 [1,0,9,2,1] 。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、1 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/separate-the-digits-in-an-array/
"""
from typing import List


class Solution:

    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            while num:
                ans.append(num % 10)
                num //= 10
        return ans[::-1]


if __name__ == '__main__':
    # [1,3,2,5,8,3,7,7]
    print(Solution().separateDigits([13, 25, 83, 77]))
    # [7,1,3,9]
    print(Solution().separateDigits([7, 1, 3, 9]))
