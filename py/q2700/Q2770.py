"""
 * 给你一个下标从 0 开始、由 n 个整数组成的数组 nums 和一个整数 target 。
 * 你的初始位置在下标 0 。在一步操作中，你可以从下标 i 跳跃到任意满足下述条件的下标 j ：
 * 1、0 <= i < j < n
 * 2、-target <= nums[j] - nums[i] <= target
 * 返回到达下标 n - 1 处所需的 最大跳跃次数 。
 * 如果无法到达下标 n - 1 ，返回 -1 。
 * 提示：
 * 1、2 <= nums.length == n <= 1000
 * 2、-10^9 <= nums[i] <= 10^9
 * 3、0 <= target <= 2 * 10^9
 * 链接：https://leetcode.cn/problems/maximum-number-of-jumps-to-reach-the-last-index/
"""
from typing import List


class Solution:

    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dis = [-1] * n
        dis[-1] = 0
        for i in range(n - 1, 0, -1):
            if (dis[i] == -1):
                continue
            for j in range(i - 1, -1, -1):
                if abs(nums[i] - nums[j]) > target:
                    continue
                dis[j] = max(dis[j], dis[i] + 1)
        return dis[0]


if __name__ == '__main__':
    # 3
    print(Solution().maximumJumps([1, 3, 6, 4, 1, 2], target=2))
    # 5
    print(Solution().maximumJumps([1, 3, 6, 4, 1, 2], target=3))
    # -1
    print(Solution().maximumJumps([1, 3, 6, 4, 1, 2], target=0))
