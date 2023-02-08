"""
 * 沿街有一排连续的房屋。每间房屋内都藏有一定的现金。现在有一位小偷计划从这些房屋中窃取现金。
 * 由于相邻的房屋装有相互连通的防盗系统，所以小偷 不会窃取相邻的房屋 。
 * 小偷的 窃取能力 定义为他在窃取过程中能从单间房屋中窃取的 最大金额 。
 * 给你一个整数数组 nums 表示每间房屋存放的现金金额。形式上，从左起第 i 间房屋中放有 nums[i] 美元。
 * 另给你一个整数数组 k ，表示窃贼将会窃取的 最少 房屋数。小偷总能窃取至少 k 间房屋。
 * 返回小偷的 最小 窃取能力。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、1 <= k <= (nums.length + 1)/2
 * 链接：https://leetcode.cn/problems/house-robber-iv/
"""
from typing import List


class Solution:

    def minCapability(self, nums: List[int], k: int) -> int:
        ans = 0

        def calc(v):
            ret, cnt = 0, 0
            for num in nums:
                if v >= num:
                    cnt += 1
                else:
                    ret += cnt // 2 + cnt % 2
                    cnt = 0
            return ret + cnt // 2 + cnt % 2

        l, r = 0, 10**2
        while l <= r:
            mid = l + (r - l) // 2
            sum = calc(mid)
            if sum >= k:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


if __name__ == '__main__':
    # 71
    print(Solution().minCapability([35, 9, 18, 78, 40, 8, 71, 2, 59], 5))
    # 5
    print(Solution().minCapability([2, 3, 5, 9], 2))
    # 2
    print(Solution().minCapability([2, 7, 9, 3, 1], 2))
