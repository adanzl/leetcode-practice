"""
 * 给你一个整数 n 。按下述规则生成一个长度为 n + 1 的数组 nums ：
 * 1、nums[0] = 0
 * 2、nums[1] = 1
 * 3、当 2 <= 2 * i <= n 时，nums[2 * i] = nums[i]
 * 4、当 2 <= 2 * i + 1 <= n 时，nums[2 * i + 1] = nums[i] + nums[i + 1]
 * 返回生成数组 nums 中的 最大 值。
 * 提示：0 <= n <= 100
 * 链接：https://leetcode.cn/problems/get-maximum-in-generated-array/
"""


class Solution:

    def getMaximumGenerated(self, n: int) -> int:
        if n == 0: return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(1, n):
            if i * 2 <= n: nums[i * 2] = nums[i]
            if i * 2 - 1 <= n: nums[i * 2 - 1] = nums[i - 1] + nums[i]
        return max(nums)


if __name__ == '__main__':
    # 3
    print(Solution().getMaximumGenerated(7))
    # 1
    print(Solution().getMaximumGenerated(2))
    # 2
    print(Solution().getMaximumGenerated(3))
    # 0
    print(Solution().getMaximumGenerated(0))