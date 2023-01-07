"""
 * 给你一个整数数组 nums 。你需要选择 恰好 一个下标（下标从 0 开始）并删除对应的元素。请注意剩下元素的下标可能会因为删除操作而发生改变。
 * 比方说，如果 nums = [6,1,7,4,1] ，那么：
 * 1、选择删除下标 1 ，剩下的数组为 nums = [6,7,4,1] 。
 * 2、选择删除下标 2 ，剩下的数组为 nums = [6,1,4,1] 。
 * 3、选择删除下标 4 ，剩下的数组为 nums = [6,1,7,4] 。
 * 如果一个数组满足奇数下标元素的和与偶数下标元素的和相等，该数组就是一个 平衡数组 。
 * 请你返回删除操作后，剩下的数组 nums 是 平衡数组 的 方案数 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^4
 * 链接：https://leetcode.cn/problems/ways-to-make-a-fair-array/
"""
from typing import List


class Solution:

    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        sm_even, sm_odd = [0] * (n + 1), [0] * (n + 1)
        for i in range(n):
            if i % 2 == 0:
                sm_even[i + 1] = sm_even[i] + nums[i]
                sm_odd[i + 1] = sm_odd[i]
            else:
                sm_odd[i + 1] = sm_odd[i] + nums[i]
                sm_even[i + 1] = sm_even[i]
        ans = 0
        for i in range(n):
            if sm_even[i] + sm_odd[n] - sm_odd[i + 1] == sm_odd[i] + sm_even[n] - sm_even[i + 1]:
                ans += 1
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().waysToMakeFair([2, 1, 6, 4]))
    # 3
    print(Solution().waysToMakeFair([1, 1, 1]))
    # 0
    print(Solution().waysToMakeFair([1, 2, 3]))
