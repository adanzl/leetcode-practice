"""
 * 给你一个长度为 n 的整数数组 nums 。
 * 你的目标是从下标 0 出发，到达下标 n - 1 处。每次你只能移动到 更大 的下标处。
 * 从下标 i 跳到下标 j 的得分为 (j - i) * nums[i] 。
 * 请你返回你到达最后一个下标处能得到的 最大总得分 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/reach-end-of-array-with-max-score/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def findMaximumScore(self, nums: List[int]) -> int:
        ans, val = 0, 0
        for num in nums:
            ans += val
            val = max(val, num)
        return ans


if __name__ == '__main__':
    # 7
    print(Solution().findMaximumScore([1, 3, 1, 5]))
    # 16
    print(Solution().findMaximumScore([4, 3, 1, 3, 2]))