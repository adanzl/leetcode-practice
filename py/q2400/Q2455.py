"""
 * 给你一个由正整数组成的整数数组 nums ，返回其中可被 3 整除的所有偶数的平均值。
 * 注意：n 个元素的平均值等于 n 个元素 求和 再除以 n ，结果 向下取整 到最接近的整数。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、1 <= nums[i] <= 1000
 * 链接：https://leetcode.cn/problems/average-value-of-even-numbers-that-are-divisible-by-three/
"""
from typing import List


class Solution:

    def averageValue(self, nums: List[int]) -> int:
        n, sm = 0, 0
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                n += 1
                sm += num
        return 0 if n == 0 else sm // n


if __name__ == '__main__':
    # 9
    print(Solution().averageValue([1, 3, 6, 10, 12, 15]))
    # 0
    print(Solution().averageValue([1, 2, 4, 7, 10]))
