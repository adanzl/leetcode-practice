"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个整数 p 。请你从 nums 中找到 p 个下标对，每个下标对对应数值取差值，你需要使得这 p 个差值的 最大值 最小。
 * 同时，你需要确保每个下标在这 p 个下标对中最多出现一次。
 * 对于一个下标对 i 和 j ，这一对的差值为 |nums[i] - nums[j]| ，其中 |x| 表示 x 的 绝对值 。
 * 请你返回 p 个下标对对应数值 最大差值 的 最小值 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^9
 * 3、0 <= p <= (nums.length)/2
 * 链接：https://leetcode.cn/problems/minimize-the-maximum-difference-of-pairs/
"""
from typing import List


class Solution:

    def minimizeMax(self, nums: List[int], p: int) -> int:
        ans, n = -1, len(nums)
        nums.sort()
        if n == 1: return 0
        l, r = 0, 10**9
        while l <= r:
            mid = (l + r) // 2
            sm = [0] * (n + 1)
            for i in range(1, n):
                sm[i + 1] = max(sm[i - 1], sm[i])
                if nums[i] - nums[i - 1] <= mid:
                    sm[i + 1] = max(sm[i - 1] + 1, sm[i])
            if sm[-1] >= p or sm[-2] >= p:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().minimizeMax([10, 1, 2, 7, 1, 3], p=2))
    # 0
    print(Solution().minimizeMax([4, 2, 1, 2], p=1))
