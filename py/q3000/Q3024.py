"""
 * 给你一个下标从 0 开始长度为 3 的整数数组 nums ，需要用它们来构造三角形。
 * 1、如果一个三角形的所有边长度相等，那么这个三角形称为 equilateral 。
 * 2、如果一个三角形恰好有两条边长度相等，那么这个三角形称为 isosceles 。
 * 3、如果一个三角形三条边的长度互不相同，那么这个三角形称为 scalene 。
 * 如果这个数组无法构成一个三角形，请你返回字符串 "none" ，否则返回一个字符串表示这个三角形的类型。
 * 提示：
 * 1、nums.length == 3
 * 2、1 <= nums[i] <= 100 
 * 链接：https://leetcode.cn/problems/type-of-triangle/
"""
from typing import List


class Solution:

    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)
        if a + b <= c or a + c <= b or b + c <= a:
            return 'none'
        elif a == b and b == c:
            return 'equilateral'
        elif a == b or b == c or c == a:
            return 'isosceles'
        return 'scalene'


if __name__ == '__main__':
    # 'equilateral'
    print(Solution().triangleType([3, 3, 3]))
    # 'scalene'
    print(Solution().triangleType([3, 4, 5]))
