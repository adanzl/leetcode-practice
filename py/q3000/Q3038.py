"""
 * 给你一个整数数组 nums ，如果 nums 至少 包含 2 个元素，你可以执行以下操作：
 * 选择 nums 中的前两个元素并将它们删除。
 * 一次操作的 分数 是被删除元素的和。
 * 在确保 所有操作分数相同 的前提下，请你求出 最多 能进行多少次操作。
 * 请你返回按照上述要求 最多 可以进行的操作次数。
 * 提示：
 * 1、2 <= nums.length <= 100
 * 2、1 <= nums[i] <= 1000
 * 链接：https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-i/description/
"""
from typing import Deque, List


class Solution:

    def maxOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        ans = 1
        q = Deque(nums[2:])
        sm = nums[0] + nums[1]
        while len(q) >= 2 and q[0] + q[1] == sm:
            ans += 1
            q.popleft()
            q.popleft()
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().maxOperations([3, 2, 1, 4, 5]))
    # 1
    print(Solution().maxOperations([3, 2, 6, 1, 4]))
    #
    # print(Solution().maxOperations())
